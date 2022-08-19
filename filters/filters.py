import os, sys
from PIL import Image, ImageFilter
from PIL import ImageFont, ImageDraw

# Image class to connect with discord bot
# Needs little bit of math to make the resizing fit
class ImageMagic():
    def __init__(self, img):
        self.img = img
        #self.image = Image.open(image)
        #self.image.show()

    def resize(self, x, y):
        resized = self.resize(((x, y)), resample=0)#.show()
        return resized

    def boxblur(self, radius):
        blurred = self.filter(ImageFilter.BoxBlur(radius))
        return blurred

    def gaussianblur(self, radius):
        blurred = self.filter(ImageFilter.GaussianBlur(radius))
        return blurred

    def unsharpmask(self, radius, percent, threshold):
        unsharpmasked = self.filter(ImageFilter.BoxBlur(radius))
        return unsharpmasked

    def getbox(self):
        with self as im:
            box = im.getbbox()
        return box

    def getdata(self):
        getdata = self.getdata()
        return getdata

    def quantize(self, colors):
        quantize = self.quantize(colors)
        return quantize

