# -*- coding: utf-8 -*-
# This file is part of pytablefy
#
# A python svg table library
# Copyright  © 2013 Fayiz Musthafa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the "Software"), to deal in the Software 
# without restriction, including without limitation the rights to use, copy, modify, merge
# ,publish, distribute, sublicense, and/or sell copies of the Software, and to permit 
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
# OR OTHER DEALINGS IN THE SOFTWARE.

class Style(object):
    ''' Style class'''
    def __init__(
            self,
            background='white',
            background_stroke='white'
            column_background='#E20000',
            column_stroke='white',
            row_background='white',
            row_stroke='black',
            background_opacity='0.9',
            stroke_opacity='0.6'
            ):
        self.background = background
        self.background_stroke = background_stroke
        self.column_background = column_background
        self.column_stroke = column_stroke
        self.row_background = row_background
        self.row_stroke = row_stroke
        self.background_opacity = background_opacity
        self.stroke_opacity = stroke_opacity

defaultstyle = Style()                 


