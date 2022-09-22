import numpy as np

def pio(z):
    """
    positive incident overpressure for Surface Burst
    z: m/kg^(1/3)
    pio (Peak overpressure): MPa ---> kPa
    """ 

    c1 = np.flipud(np.array([1.3295e-1, -2.1712, -1.3878, -1.0401, -3.7148e-1]))    
    c2 = np.flipud(np.array([1.3067e-1, -2.0672, -1.1750, 2.1159, -8.3460e-1]))    
    c3 = np.flipud(np.array([7.8363e-1, -4.5738, 2.6834, -7.2311e-1, 0.]))  
    
    ans = np.zeros(z.shape[0])      
    ans1 = np.where( ((0.06 <= z) & (z <= 1.13)), np.polyval(c1, np.log10(z)), ans)
    ans2 = np.where(((1.13 < z) & (z <= 10.)), np.polyval(c2, np.log10(z)), ans1)
    ans3 = np.where(((10. < z) & (z <= 40.)), np.polyval(c3, np.log10(z)), ans2)
    
    ans = 1000 * 10**ans3
    
    return ans
  
def toa(z):
    """
    z: m/kg^(1/3)
    toa (Time of arrival, scaled): ms/kg^(1/3)
    """ 
    c1 = np.flipud(np.array([-3.3217e-1, 1.8061, 4.3653e-1, 2.6277e-1, 1.5906e-1]))    
    c2 = np.flipud(np.array([-3.5217e-1, 1.9914, -1.3049e-1, -1.7628e-1, 0.]))    
    c3 = np.flipud(np.array([-7.4315e-2, 1.5680, -1.5812e-1, 0., 0.]))  

    ans = np.zeros(z.shape[0])      
    ans1 = np.where( ((0.06 <= z) & (z <= 1.46)), np.polyval(c1, np.log10(z)), ans)
    ans2 = np.where(((1.46 < z) & (z <= 10.)), np.polyval(c2, np.log10(z)), ans1)
    ans3 = np.where(((10. < z) & (z <= 40.)), np.polyval(c3, np.log10(z)), ans2)
    ans = 10**ans3
    
    return ans 

def ppd(z):
    """
    positive_phase_duration, scaled
    z: m/kg^(1/3)
    positive_phase_duration: ms/kg^(1/3)
    """
    c1 = np.flipud(np.array([4.3227e-1, 6.1103, 12.418, 11.021, 3.8670]))    
    c2 = np.flipud(np.array([2.4242e-1, 3.6673, 2.6397, 0., 0.]))    
    c3 = np.flipud(np.array([2.4255e-1, 2.1849, -14.917, 35.106, -23.852]))  
    c4 = np.flipud(np.array([-3.2552e-1, 2.7174, -2.7949, 1.0846, 0.]))
    c5 = np.flipud(np.array([2.7214e-1, 4.8449e-1, -7.6501e-2, 0., 0.]))

    ans = np.zeros(z.shape[0])      
    ans1 = np.where(((0.17 <= z) & (z <= 0.69)), np.polyval(c1, np.log10(z)), ans)
    ans2 = np.where(((0.69 < z) & (z <= 1.00)), np.polyval(c2, np.log10(z)), ans1)
    ans3 = np.where(((1.00 < z) & (z <= 2.88)), np.polyval(c3, np.log10(z)), ans2)
    ans4 = np.where(((2.88 < z) & (z <= 10. )), np.polyval(c4, np.log10(z)), ans3)
    ans5 = np.where(((10.0 < z) & (z <= 40.0)), np.polyval(c5, np.log10(z)), ans4)
    ans = 10**ans5

    return ans 
           

