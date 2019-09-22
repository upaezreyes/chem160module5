from math import pi, cos, sqrt

dt = 0.001   # Change of time
mass = 10  # mass of the pendulum
period = 10 # period of the pendulum
omega = 2*pi/period
k = mass*omega**2   # spring constant (k)
tmax = period   # t = period
x= +1    # initial position of the pendulum
v = 0    # initial velocity 
t = 0    # initial time 
rms_error = 0  # keep track of the sum of the exact and numerical value
steps = 0   # keep count of the total number of steps

while t<tmax:   # stops the loop when t>tmax
    f = -k*x  #magnitude of the force applied on the pendulum
    a = f/mass  # acceleration of the pendulum
    x += v*dt   # update the possition of the pendulum
    v += a*dt   # update the velocity of the pendulum

    x_exact = cos(2*pi*t/period)  # exact value of the position of the pendulum
    rms_error += (x-x_exact)**2   # calculates the error bwt exact and numerical values
    steps += 1   # steps taken 
    t += dt     # implement the time

print("dt=%f RMS error=%f"%(dt,sqrt(rms_error/steps)))
