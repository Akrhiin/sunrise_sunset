# File: read_sunrises.py
# Date: 2020-11-30
# Author: Michael Pace

# imports
import os
import numpy as np
import cv2 as cv

# select directory
count = 1
for filename in os.listdir('sunrises'):
    # read image
    sunrise_img = cv.resize(cv.imread(os.path.join('sunrises', filename)), (15, 15))
    # convert to array
    sunrise_colors = np.array(sunrise_img, dtype=np.float32)
    sunrise_colors = sunrise_colors.reshape(-1, 3)

    # test - uncomment to print colors
    # print(colors)

    # open file
    with open('sunrises_data/sunrise' + str(count) + '.txt', 'w') as file:
        for color in sunrise_colors:
            # write color to file
            file.write(str(color) + '\n')
    #close file
    file.close()
    # increment file count
    count += 1
    