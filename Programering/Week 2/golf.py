import math

velocity=20 #v0
theta=45*(math.pi/180) #radianer
acceleration=9.821 #m/s**2

#range
range=round(((velocity**2)*math.sin(2*theta))/(acceleration))

#Time
vy=velocity*math.sin(theta)

time=round((2*vy)/acceleration, 2)

print("Range: "+str(range)+" meter(s). Time of flight: "+str(time)+" second(s).")
