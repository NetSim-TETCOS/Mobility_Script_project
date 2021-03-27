import random
import math
import sys

#variable declaration
array=[]
vel = []
x = []
y = []

#mobility file generated for linear or circular case
lc = "Circular"

#Total number of devices used in geneartion of mobility.txt file
n=7
#list of device id's(deviceid - 1) present in the file
deviceid=[8,9,10,11,12,13,14]

#steps in distance
distanceStep = 0.5 

#time gap between two location
timeStep =5.0 
timeperStep = 3

#range at which time will add into mobility.txt file
lengthOfsteps = 1801

#velocity at which devices are moving
velocity = 8.0 

#initial position of device
x_coordinates = 280.0 
y_coordinates = 400.0 

#grid length 
grid_min = 0.0
grid_max_x = 1000.0 
grid_max_y = 1000.0 


for i in range(0,n):
    vel.append(velocity)
    x.append(x_coordinates)
    y.append(y_coordinates)
  
def condition(x,y):
    if x<grid_min or x>grid_max_x or y<grid_min or y>grid_max_y:
        return 0 #invalid grid length value
    else:
        return 1

def generaterandominteger_C(x,y,dperstep,angle):
    print(dperstep)
    print(angle)
    a=x+(dperstep*math.cos(angle)) 
    b=y+(dperstep*math.sin(angle))
  
    if condition(a,b)==1:
        return (a,b,angle)
    else:
        rint=random.randint(0,360)   
        newangle=math.radians(rint)
        angle=newangle
        print("Recursion here %.1f %.1f " % (x,y))
        return generaterandominteger_C(x,y,dperstep,angle)
    
def generaterandominteger_L(x,y,dperstep):
    print(dperstep)
    a=x
    b=y + dperstep

    return (a,b)
   
    
for i in range(n):
    dperstep=vel[i]* distanceStep
    print("velocity and dperstep is %f %f" % (vel[i],dperstep))
    array.append("$time 0.0 \"$node_(%d) %.1f %.1f 0.0\""%(deviceid[i]-1,x[i],y[i]))
    rint=random.randint(0,360)
    angle=math.radians(rint)
    for j in range(1,lengthOfsteps):
        if(j%timeperStep==0):
           time=j/timeStep #time at which device will move.
           x1=x[i]
           y1=y[i]
           angle1=angle
           print("x and y values are %f %f "%(x1,y1))
           if lc == "Linear":
               x[i],y[i]=generaterandominteger_L(x1,y1,dperstep)
           else:
               x[i],y[i],angle=generaterandominteger_C(x1,y1,dperstep,angle1)
           if condition(x[i],y[i])==0:
               break
               
           array.append("$time %.1f \"$node_(%d) %.1f %.1f 0.0\""%(time,deviceid[i]-1,x[i],y[i]))
           print("x[] and y[] values are %f %f "%(x[i],y[i]))
      

print(array)
f= open("mobility.txt","w")
for line in array:
    f.writelines(line)
    f.writelines('\n')
f.close()   
     
