
from xml.etree import ElementTree as et

class Svg(object):
    def __init__(self, width, height, background):
        self.width = str(width)
        self.height = str(height)
        self.background = background
        self.svgdata = et.Element('svg', width=self.width, height=self.height, version='1.1', xmlns='http://www.w3.org/2000/svg')
        self.rect(self.background)
