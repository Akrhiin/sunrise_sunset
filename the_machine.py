# File: the_machine.py
# Date: 2020-11-30
# Author: Michael Pace

# imports
import os
import sys
import numpy as np
import sklearn as sk

# numpy settings ----------------------------------------------
np.set_printoptions(threshold=sys.maxsize)

# sunrises ====================================================
sunrise_colors = []
for filename in os.listdir('sunrises_data'):
    # open file
    with open(os.path.join('sunrises_data', filename), 'r') as file:
        # read file
        colors = file.readlines()
        # convert to array
        colors = np.array([np.fromstring(color.strip('[]'), dtype=np.float32, sep=' ') for color in colors])
        # append to list
        sunrise_colors.append(colors)
# close file
file.close()
# flatten list
sunrise_colors = np.array(sunrise_colors).reshape(-1, 3)

# test - uncomment to print sunrise_colors
# print(sunrise_colors)

# sunsets =====================================================
sunset_colors = []
for filename in os.listdir('sunsets_data'):
    # open file
    with open(os.path.join('sunsets_data', filename), 'r') as file:
        # read file
        colors = file.readlines()
        # convert to array
        colors = np.array([np.fromstring(color.strip('[]'), dtype=np.float32, sep=' ') for color in colors])
        # append to list
        sunset_colors.append(colors)
# close file
file.close()
# flatten list
sunset_colors = np.array(sunset_colors).reshape(-1, 3)

# test - uncomment to print sunset_colors
# print(sunset_colors)

# model =======================================================

#    *insert model here*