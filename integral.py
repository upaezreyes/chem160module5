from math import exp
def f(x):
    return x*exp(-x)


# Numerically Integrated f(x) from 0 to 50
intgrl = 0.0   # sum the area of the integration
x = 0    # lower bound of the integral
xmax = 50  # upper bound of the itegral
dx = 0.001  # step space

while x<xmax:  # break the while loop when x > xmax
    intgrl += dx*f(x)
    x += dx
print("Ingetral(Area of x*exp(-x)=",intgrl,"Error=",abs(1-intgrl))
