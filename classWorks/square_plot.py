#!/bin/env python3.8    
# This is where our python file is......usually its in #!usr/bin/env python3.8#
###############################################################################
###########################import required modules#############################
import numpy as np
import matplotlib.pyplot as plt
###############################################################################
x = np.arange(100)
y = x**2
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('X**2')
plt.show()
###############################################################################
