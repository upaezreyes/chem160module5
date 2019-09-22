import sys
import math
def distance(p1, p2):  # accepts points from any dimension(1D, 2D or 2D)
    if len(p1) != len(p2):   # if the points are from different dimensions, it will not run
        sys.exit("Vectors have different length")
    sum = 0

    for i in range(len(p1)):   # Loop over the side of the vector 
        sum += (p1[i] - p2[i])**2   # Sum up the square difference of each vector
    return math.sqrt(sum)   # sqrt the distance
