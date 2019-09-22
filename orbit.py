from math import sqrt
from drawtraj import drawtraj   # to draw the trajectory
def force(x,y,m,mstar):   # x and y are the position of the planet and star
    r2=x**2+y**2
    r32=r2*sqrt(r2)     # distance bwt the planet and the star
    fx=-x*m*mstar/r32   # force on the x-direction
    fy=-y*m*mstar/r32   # force on the y-direction
    return fx,fy       # solve fx and fy
def integrate(x,y,vx,vy,fx,fy,m,dt):
   ax,ay = fx/m, fy/m   # aceleration on the x and y directions
   vx += ax*dt    # updating velocity on the x-direction
   vy += ay*dt    # updating velocity on the y-direction
   x += vx*dt     # updating position on the x-direction
   y += vy*dt     # updation position on the y-direction
   return x, y, vx, vy

# Main part of the program
mstar = 1000    # mass of the star (100 bigger than the planet
m = 10        # mass of the planet
nsteps = 100000  # steps
dt = 0.01    # space steps of time
r = 60       # radius (distance from the planet and star)
x,y = 0,r    # positions of the planet and star
vx,vy = 1.2,0.6  # Initial velocities
trajx,trajy=[],[]

for t in range(nsteps):
    fx,fy = force(x,y,m,mstar)  # calculates fx & fy using the force function
    x,y,vx,vy, = integrate(x,y,vx,vy,fx,fy,m,dt)
    trajx.append(x)
    trajy.append(y)

drawtraj(trajx,trajy,10*r)   #side of the box