from base64 import b64decode
import base64
from rest_framework import views, status
from rest_framework.response import Response
from math import log10 
from .libblast import surface_burst, plotter

import numpy as np

from .serializer import BlastRequestSerializer

# 爆発電卓API
class BlastRetrieveView(views.APIView):

    def get(self, request, format=None):
        serializer = BlastRequestSerializer(data=request.GET)
        
        if (serializer.is_valid()):
            exp_weight = serializer.validated_data['exp_weight']
            exp_er = serializer.validated_data['exp_er']
            add_tnt = serializer.validated_data['add_tnt']
            meas_points = serializer.validated_data['meas_points']

            # 爆風電卓 提供ロジック ここから ===============================================
            meas_points = np.array([float(x.strip()) for x in meas_points.split(',')])  
            
            ### Default values
            extend = 1.2 # plot range xmin/extend -- xmax*extend
            npoint = 200 # curve plot 200 points Default

            ###
            total_tnt = exp_weight * exp_er + add_tnt
            tnt13 = total_tnt**(1/3)
            Nmeas_points = meas_points.shape[0]
            plot_range = np.array([np.min(meas_points)/extend, np.max(meas_points)*extend]) 


            ##################################
            # line and scatter data  
            xlinestart = log10(plot_range[0])
            xlinestop = log10(plot_range[1])

            xline = 10**(np.linspace(xlinestart, xlinestop, npoint))
            y0line0 = surface_burst.pio(xline/tnt13)
            y1line0 = surface_burst.toa(xline/tnt13)*tnt13
            y1line1 = y1line0 + surface_burst.ppd(xline/tnt13)*tnt13
            y1line2 = y1line0 + 5*surface_burst.ppd(xline/tnt13)*tnt13

            xscatter = meas_points
            y0scatter0 = surface_burst.pio(xscatter/tnt13)
            y1scatter0 = surface_burst.toa(xscatter/tnt13)*tnt13
            y1scatter1 = y1scatter0 + surface_burst.ppd(xscatter/tnt13)*tnt13
            y1scatter2 = y1scatter0 + 5*surface_burst.ppd(xscatter/tnt13)*tnt13

            ###
            result = []
            for i in range(xscatter.shape[0]):
                #print("At %6.2f [m], pio = %9.2e [kPaG], toa+5ppd = %9.2e [ms]"% \
                #    (xscatter[i], y0scatter0[i], y1scatter2[i])), 
                result.append([xscatter[i], y0scatter0[i], y1scatter2[i]])
            ###
            ##################################
            # plot
            pltr = plotter.PlotBlast()
            pltr.line_plot(0, xline, y0line0, 'pio', 'upper right')
            pltr.line_plot(1, xline, y1line0, 'toa', 'upper left')
            pltr.line_plot(1, xline, y1line1, 'toa+ppd', 'upper left')
            pltr.line_plot(1, xline, y1line2, 'toa+5*ppd', 'upper left')

            pltr.scatter_plot(0, xscatter, y0scatter0, 'pio', 'upper right')
            pltr.scatter_plot(1, xscatter, y1scatter0, 'toa', 'upper left')
            pltr.scatter_plot(1, xscatter, y1scatter1, 'toa+ppd', 'upper left')
            pltr.scatter_plot(1, xscatter, y1scatter2, 'toa+5*ppd', 'upper left')
            # pltr.plot_show()
            # 爆風電卓 提供ロジック ここまで ===============================================

            # response_data = {'results': result,'result_img': "data:image/png;base64,"+base64.b64encode(pltr.get_plot()).decode()}
            response_data = {'results': result,'result_img': base64.b64encode(pltr.get_plot()).decode()}

            return Response(response_data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
