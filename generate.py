#!/usr/bin/env python

from datetime import datetime
from numpy import *
import numpy as np
from PIL import Image


WHITE = 255.0
BLACK = 0.0
dpiy = 5000
dpix = 2* dpiy
y = linspace(1, 0, dpix)
x = linspace(-1.5,0.5,dpiy)

xv, yv = meshgrid(x,y)

# Turn coordinates into one array of complex numbers
z = xv + yv*1j

# Set value of c to initial value of complex numbers
# We are trying to find c_n < 2 as members of M(andelbrot Set)
c = z

# Counter matrix - keeps track of how many iterations it takes before a
# point leaves the Mandelbrot set 
counter = zeros(c.shape)
zero = zeros(c.shape)
ident = ones(c.shape)

iters = 1000.0
for i in range(int(iters)):
    print (float(i)/iters)*100

    # Do calculation
    z = multiply(z,z) + c

    # Find all values with a abs value greater than 2
    filter = abs(z) > 2

    # Add set the current iteration as their value in counter matrix
    # i.e. record the iteration during which they escaped.
    counter = where(filter, i*ident, counter) 

    # TODO: Set values of escaped points to 0 in z and c
    
    z = where(filter, zero, z)
    c = where(filter, zero, c)
    

    
max_val =  amax(counter)
print max_val


# Scale the counter matrix to the maximum colour value (e.g. WHITE)
counter = (counter/max_val)*WHITE

# Save as picture :)
im = Image.fromarray(counter)
im = im.convert('RGB')
im.save("Mandelbrot.png")

fname = "{0}.{1}.{2}.npy".format(str(dpix), str(dpiy),
        datetime.now().strftime("%d%m%y.%H%M%S"))
f = open(fname)
np.save(f, counter)
f.close()
