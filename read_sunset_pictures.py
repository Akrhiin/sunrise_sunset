# File: read_sunsets.py
# Date: 2020-11-30
# Author: Michael Pace

# imports
import os
import numpy as np
import cv2 as cv

# select directory
count = 1
for filename in os.listdir('sunsets'):
    # read image
    sunset_img = cv.resize(cv.imread(os.path.join('sunsets', filename)), (15, 15))
    # convert to array
    sunset_colors = np.array(sunset_img, dtype=np.float32)
    sunset_colors = sunset_colors.reshape(-1, 3)

    # test - uncomment to print colors
    # print(colors)

    # open file
    with open('sunsets_data/sunset' + str(count) + '.txt', 'w') as file:
        for color in sunset_colors:
            # write color to file
            file.write(str(color) + '\n')
    #close file
    file.close()
    # increment file count
    count += 1