#!/usr/bin/env python
"""
  This module tests the function of Polygon vertices Generation.
  TODO test_concavePolygon and test_convexPolygon
"""

import unittest
import os

from blocksWorld import *

imageSize = (640, 480)
imageMode = 'L'
imageBackground = 'white'

fileType = 'PNG'
fileDir = os.path.dirname(os.path.realpath('__file__'))
directory = os.path.join(fileDir, '../data/polygon')

if not os.path.exists(directory):
    os.makedirs(directory)

points = np.array([
    [5,  5],
    [5, 15],
    [5, 25],
    [5, 35],
    [5, 45],
    [5, 55],
    [5, 65],
    [5, 75]
])

class test_polygon(unittest.TestCase):

    """
        Ploting Images for different types of polygons.
    """

    # Reference images for regularPolygon.
    def test_regularPolygon(self):
        # Reference image for regularPolygon
        regularImage = Image.new(imageMode, imageSize, imageBackground)
        regularCanvas = ImageDraw.Draw(regularImage)

        draw(regularCanvas, regularPolygon(3, np.array([160, 120]), 50), '3')
        draw(regularCanvas, regularPolygon(4, np.array([480, 120]), 90), '4')
        draw(regularCanvas, regularPolygon(5, np.array([420, 360]), 60), '5')
        draw(regularCanvas, regularPolygon(6, np.array([160, 360]), 80), '6')
        draw(regularCanvas, regularPolygon(7, np.array([320, 160]), 70), '7')

        fileName = 'test_regularPolygon.png'

        regularImage.save(directory+"/"+fileName, fileType)
        regularImage.close()

        # Reference image for regularPolygon with rotated points
        regularRotatedImage = Image.new(imageMode, imageSize, imageBackground)
        regularRotatedCanvas = ImageDraw.Draw(regularRotatedImage)

        center = np.array([320, 240])
        draw(regularRotatedCanvas, [center], 'center')

        draw(regularRotatedCanvas, (rotate((regularPolygon(3, np.array([160, 120]), 50)), center, 45.0)), '3r')
        draw(regularRotatedCanvas, (rotate((regularPolygon(4, np.array([480, 120]), 90)), center, 45.0)), '4r')
        draw(regularRotatedCanvas, (rotate((regularPolygon(5, np.array([420, 360]), 60)), center, 45.0)), '5r')
        draw(regularRotatedCanvas, (rotate((regularPolygon(6, np.array([160, 360]), 80)), center, 45.0)), '6r')
        draw(regularRotatedCanvas, (rotate((regularPolygon(7, np.array([320, 160]), 70)), center, 45.0)), '7r')

        fileName = 'test_regularRotatedPolygon.png'

        regularRotatedImage.save(directory + "/" + fileName, fileType)
        regularRotatedImage.close()

        # Reference image for regularPolygon with wire
        regularWiredImage = Image.new(imageMode, imageSize, imageBackground)
        regularWiredCanvas = ImageDraw.Draw(regularWiredImage)

        drawWire(regularWiredCanvas, regularPolygon(3, np.array([160, 120]), 50))
        drawWire(regularWiredCanvas, regularPolygon(4, np.array([480, 120]), 90))
        drawWire(regularWiredCanvas, regularPolygon(5, np.array([420, 360]), 60))
        drawWire(regularWiredCanvas, regularPolygon(6, np.array([160, 360]), 80))
        drawWire(regularWiredCanvas, regularPolygon(7, np.array([320, 160]), 70))

        fileName = 'test_regularWiredPolygon.png'

        regularWiredImage.save(directory + "/" + fileName, fileType)
        regularWiredImage.close()

        # Reference image for regularPolygon using rotated points with wire
        regularRotatedWiredImage = Image.new(imageMode, imageSize, imageBackground)
        regularRotatedWiredCanvas = ImageDraw.Draw(regularRotatedWiredImage)

        center = np.array([320, 240])
        draw(regularRotatedWiredCanvas, [center], 'center')

        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(3, np.array([160, 120]), 50)), center, 45.0)))
        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(4, np.array([480, 120]), 90)), center, 45.0)))
        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(5, np.array([420, 360]), 60)), center, 45.0)))
        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(6, np.array([160, 360]), 80)), center, 45.0)))
        drawWire(regularRotatedWiredCanvas, (rotate((regularPolygon(7, np.array([320, 160]), 70)), center, 45.0)))

        fileName = 'test_regularRotatedWiredPolygon.png'

        regularRotatedWiredImage.save(directory + "/" + fileName, fileType)
        regularRotatedWiredImage.close()

        # Reference image for combined shapes
        shapeImage = Image.new(imageMode, imageSize, imageBackground)
        shapeCanvas = ImageDraw.Draw(shapeImage)

        drawWire(shapeCanvas, (rotate((regularPolygon(3, np.array([320, 240]), 110)), np.array([450, 200]), 30.0)))
        drawWire(shapeCanvas, (rotate((regularPolygon(4, np.array([320, 240]), 120)), center, 45.0)))

        fileName = 'test_shape.png'

        shapeImage.save(directory + "/" + fileName, fileType)
        shapeImage.close()

    # def test_convexPolygon(self):
    # TODO

    # def test_concavePolygon(self):
    # TODO

    # Reference imagea for randomPolygon.
    def test_randomPolygon(self):
        # Reference image for randomPolygon
        randomImage = Image.new(imageMode, imageSize, imageBackground)
        randomCanvas = ImageDraw.Draw(randomImage)

        seed = 5
        draw(randomCanvas, randomPolygon(seed, 3, np.array([160, 120]), 200), '3r')
        draw(randomCanvas, randomPolygon(seed, 4, np.array([480, 120]), 200), '4r')
        draw(randomCanvas, randomPolygon(seed, 5, np.array([480, 360]), 200), '5r')
        draw(randomCanvas, randomPolygon(seed, 6, np.array([160, 360]), 200), '6r')
        draw(randomCanvas, randomPolygon(seed, 7, np.array([320, 240]), 200), '7r')

        fileName = 'test_randomPolygon.png'

        randomImage.save(directory+"/"+fileName, fileType)
        randomImage.close()

        # Reference image for randomPolygon with rotated points
        randomRotatedImage = Image.new(imageMode, imageSize, imageBackground)
        randomRotatedCanvas = ImageDraw.Draw(randomRotatedImage)

        center = np.array([320, 240])
        draw(randomRotatedCanvas, [center], 'center')

        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 3, np.array([160, 120]), 50)), center, 90.0)), '3r')
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 4, np.array([480, 120]), 90)), center, 90.0)), '4r')
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 5, np.array([420, 360]), 60)), center, 90.0)), '5r')
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 6, np.array([160, 360]), 80)), center, 90.0)), '6r')
        draw(randomRotatedCanvas, (rotate((randomPolygon(seed, 7, np.array([320, 160]), 70)), center, 90.0)), '7r')

        fileName = 'test_RandomRotatedPolygon.png'

        randomRotatedImage.save(directory + "/" + fileName, fileType)
        randomRotatedImage.close()


if __name__ == '__main__':
    unittest.main()
