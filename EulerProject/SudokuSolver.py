import numpy as np
import matplotlib.pyplot as plt

diameter = 270

rows = 18

radius = diameter/2
dx = dy = diameter/(rows)
spacing = np.linspace(0,np.pi,rows)
xs = np.sin(spacing)

xgcode = "G1 M5 S1000 F1000 X0 Y0\n"
ygcode = ""

rowPos=0
for i in range(0,rows-1):
    rowPos+=dx
    startx = np.sqrt(radius**2-(radius-rowPos)**2)
    starty = np.sqrt(radius**2-(radius-rowPos)**2)
    
    if i%2==0:
        xgcode += "M5 F1000 X{:0.4f} Y{:0.4f}\n".format(radius+startx,rowPos)
        xgcode += "M3 F100  X{:0.4f} Y{:0.4f}\n".format(radius-startx,rowPos)
        
        ygcode += "M5 F1000 X{:0.4f} Y{:0.4f}\n".format(rowPos,radius+starty)
        ygcode += "M3 F100  X{:0.4f} Y{:0.4f}\n".format(rowPos,radius-starty)
        
    else:
        xgcode += "M5 F1000 X{:0.4f} Y{:0.4f}\n".format(radius-startx,rowPos)
        xgcode += "M3 F100  X{:0.4f} Y{:0.4f}\n".format(radius+startx,rowPos)
        
        ygcode += "M5 F1000 X{:0.4f} Y{:0.4f}\n".format(rowPos,radius-starty)
        ygcode += "M3 F100  X{:0.4f} Y{:0.4f}\n".format(rowPos,radius-starty)
    
    plt.hlines(rowPos,radius-starty,radius+starty)
    plt.vlines(rowPos,radius-startx,radius+startx)
        
    
        
    
    
gcode = xgcode+ygcode

spacing = np.linspace(0,2*np.pi,1000)
xs = np.cos(spacing)*radius+radiusju
ys = np.sin(spacing)*radius+radius

gcode+="M5 X{:0.4f} Y{:0.4f}\n".format(xs[0],ys[0])
gcode+="M3 F100\n"
for x,y in zip(xs[1:],ys[1:]):
    gcode+="X{:0.4f} Y{:0.4f}\n".format(x,y)
    
gcode+="M5 F1000 X0 Y0"
    
plt.plot(xs,ys)
plt.xlim(0,diameter)
plt.ylim(0,diameter)



plt.show()