from base64 import encode
import base64
import io
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class PlotBlast:
    def __init__(self):
        matplotlib.use('SVG')
        self.fig = plt.figure(figsize=(16, 8))
        self.fig1 = plt.figure(figsize=(6, 8))
        self.fig1, axes = plt.subplots(2)
        self.ax = ([axes[0], axes[1]])
        self.ax[0] = self.fig.add_subplot(121, title='Peak Incident Overpressure', \
                    ylabel='Overpressure (kPaG)',
                    xlabel = 'R (m)')
        self.ax[1] = self.fig.add_subplot(122, title='Time of Arrival, + ppd, + 5ppd', \
                    ylabel='Time Of Arrival, + Positive Phase Duration (ms)', 
                    xlabel = 'R (m)')
        
        self.ax[0].set_xscale('log')
        self.ax[0].set_yscale('log')
        self.ax[0].grid(which='major') 
        self.ax[0].grid(which='minor')
        self.ax[1].set_xscale('log')
        self.ax[1].set_yscale('log')
        self.ax[1].grid(which='major') 
        self.ax[1].grid(which='minor')

        return
        
    def line_plot(self, ipp, x, y, str1='Line', str2='upper left'):        
        self.ax[ipp].plot(x,y,label=str1)
        self.ax[ipp].legend(loc=str2)
        return
    
    
    def scatter_plot(self, ipp, x, y, str1='Line', str2='upper left'):     
        self.ax[ipp].scatter(x,y,label=str1)
        self.ax[ipp].legend(loc=str2)
        return


    def plot_show(self):
        self.fig.savefig("img.png")
        #plt.show()
        return

    def get_plot(self):
        buf = io.BytesIO()
        self.fig.savefig(buf, format='png')
        binary = buf.getvalue()
        print(len(base64.b64encode(binary).decode()))
        buf.close()
        return binary

if __name__ == "__main__":
    x = np.array([1,10,110])
    y = np.array([1,10,110])
    pb = PlotBlast()
    pb.line_plot(0, x, y, 'xxx', 'lower right')
    y1 = np.flipud(y)
    pb.line_plot(1, x, y1, 'yyyy')
    pb.scatter_plot(1, x, y, 'YY', 'center right')
    pb.plot_show()    
    
    
    
