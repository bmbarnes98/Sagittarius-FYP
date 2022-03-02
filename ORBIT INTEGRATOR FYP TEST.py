#Orbit Integrator fyp

import matplotlib.pyplot as plt


#constants
#Msun = 2*10**80
mass = 9
timestep = 1e-5
x = 8
y = 0
G = 4.34e+4
vx = 0
vy = 220

def fx(x,y):
    output = -G*mass*(x**2+y**2)**-(3/2)
    return output

def fy(x,y):
    output = -G*mass*(x**2+y**2)**-(3/2)
    return output

#Kick Drift Kick integrator test
def KDK_Test(x,y,vx,vy,mass):    
    x_coords = []
    y_coords = []
    vx_track = []
    vy_track = []
    
    
    for i in range(10000):
        
        #v(n+1/2)
        vx = vx + fx(x,y)*(timestep/2)
        #x(n+1)
        x = x + vx*(timestep)
        #v(n+1)
        vx = vx + fx(x,y)*(timestep/2)
        #track vx
        vx_track.append(vx)
        
        #v(n+1/2)
        vy = vy + fy(x,y)*(timestep/2)
        #y(n+1)
        y = y + vy*(timestep)
        #v(n+1)
        vy = vy + fy(x,y)*(timestep/2)
        #vy track
        vy_track.append(vy)
        
        x_coords.append(x)
        y_coords.append(y)
        
    #print(x_coords)
    #print(y_coords)
    
    plt.plot(x_coords,y_coords)
    

    
KDK_Test(x,y,vx,vy,mass)

    
    
