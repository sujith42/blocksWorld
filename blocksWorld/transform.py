# Copyright (c) 2018 Dan Petre

# The MIT License (MIT)

# https://pypi.org/project/recordtype/

"""
This module defines the following data types and methods:
- rotatePoints
"""

import math
import numpy as np

def rotate(points, center, angle):
    """
    Rotate a list of points.
    """

    output = []

    radAngle = (angle / 360.0) * 2.0 * math.pi
    c = math.cos(radAngle)
    s = math.sin(radAngle)

    for point in points:

        x = point[0] - center[0]
        y = point[1] - center[1]

        xr = x * c - y * s + center[0]
        yr = x * s + y * c + center[1]

        output.append(np.array([xr, yr]))

    return output