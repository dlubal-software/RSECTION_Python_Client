#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/..')


from RSECTION.initModel import Calculate_all, Model
from RSECTION.BasicObjects.material import Material
from RSECTION.BasicObjects.point import Point
from RSECTION.BasicObjects.line import Line
from RSECTION.BasicObjects.part import Part
from RSECTION.BasicObjects.element import Element
from RSECTION.enums import ElementArcAlphaAdjustmentTarget

if __name__ == '__main__':

    Model(True, "Steelracksystem") # crete new model called Steelracksystem

    Model.clientModel.service.begin_modification()

    Material(1, 'S235 JR G2')

    m = [-1, 1, -1, 1]

    # Creating Points
    for i in range(2):
        Point(i+1, m[i]*0.043, 0.094)
        Point(i+3, m[i]*0.0375, 0.094)
        Point(i+5, m[i]*0.032, 0.0885)
        Point(i+7, m[i]*0.032, 0.0665)
        Point(i+9, m[i]*0.0365, 0.062)
        Point(i+11, m[i]*0.064, 0.062)
        Point(i+13, m[i]*0.0685,0.0575)
        Point(i+15, m[i]*0.0685, 0.0295)
        Point(i+17, m[i]*0.0665, 0.0263)
        Point(i+19, m[i]*0.0645, 0.0232)
        Point(i+21, m[i]*0.0645, 0.0138)
        Point(i+23, m[i]*0.0665, 0.0107)
        Point(i+25, m[i]*0.0685, 0.0075)
        Point(i+27, m[i]*0.0685, 0.0025)
        Point(i+29, m[i]*0.063, -0.003)
        Point(i+31, m[i]*0.0061, -0.003)
        Point(i+33, m[i]*0.0036, -0.0017)
        
    Point(35, 0, 0)

    # Creating Points
    t = 0.0015
    n = [1, -1, -1, 1]
    for i in range(4):
        Point(i+36, m[i]*0.043, 0.094+t*n[i])
        Point(i+40, m[i]*0.0375, 0.094+t*n[i])
        Point(i+44, m[i]*0.032+t*n[i], 0.0885)
        Point(i+48, m[i]*0.032+t*n[i], 0.0665)
        Point(i+52, m[i]*0.0365, 0.062+t*n[i])
        Point(i+56, m[i]*0.064, 0.062+t*n[i])
        Point(i+60, m[i]*0.0685+t*n[i],0.0575)
        Point(i+64, m[i]*0.0685+t*n[i], 0.0295)
        Point(i+52, m[i]*0.0659, 0.0277)
        Point(i+54, m[i]*0.0671, 0.0249)
        Point(i+56, m[i]*0.0645+t*n[i], 0.0232)
        Point(i+58, m[i]*0.0645+t*n[i], 0.0138)
        Point(i+60, m[i]*0.0671, 0.0121)
        Point(i+62, m[i]*0.0659, 0.0093)
        Point(i+64, m[i]*0.0685+t*n[i], 0.0075)
        Point(i+66, m[i]*0.0685+t*n[i], 0.0025)
        Point(i+68, m[i]*0.063, -0.003+t*n[i])
        Point(i+70, m[i]*0.0061, -0.003+t*n[i])
        Point(i+72, m[i]*0.0024, -0.0027)
        Point(i+74, m[i]*0.0048, -0.0007)
        
    Point(100, 0+t, 0)
    Point(101, 0-t, 0)


    # Creating Lines     
    # for i in range(2):
    #     Line(i+1, str(i+1)+' '+ str(i+3))
    #     Line(i+3, str(i+5)+' '+ str(i+7))
    #     Line(i+5, str(i+9)+' '+ str(i+11))
    #     Line(i+7, str(i+13)+' '+ str(i+15))
    #     Line(i+9, str(i+19)+' '+ str(i+21))
    #     Line(i+11, str(i+25)+' '+ str(i+27))
    #     Line(i+13, str(i+29)+' '+ str(i+31))

    # for i in range(2):
    #     Line.Arc(15+i, [3+i, 5+i], [m[i]*0.0336, 0.0924])
    #     Line.Arc(17+i, [7+i, 9+i], [m[i]*0.0333, 0.0633])
    #     Line.Arc(19+i, [11+i, 13+i], [m[i]*0.0672, 0.0607])
    #     Line.Arc(21+i, [15+i, 17+i], [m[i]*0.068, 0.0276])
    #     Line.Arc(23+i, [17+i, 19+i], [m[i]*0.065, 0.025])
    #     Line.Arc(25+i, [21+i, 23+i], [m[i]*0.065, 0.012])
    #     Line.Arc(27+i, [23+i, 25+i], [m[i]*0.068, 0.0094])
    #     Line.Arc(29+i, [27+i, 29+i], [m[i]*0.0669, -0.0014])
    #     Line.Arc(31+i, [31+i, 33+i], [m[i]*0.0047, -0.0027])
    
    # Line.Arc(33, [33, 34], [0,0])


    thickness1 = 0.003
    # Creating Elements
    for i in range(2):
        Element(1 +i, [1+i, 3+i], thickness=thickness1)
        Element(3+i, [5+i, 7+i], thickness=thickness1)
        Element(5+i, [9+i, 11+i], thickness=thickness1)
        Element(7+i, [13+i, 15+i], thickness=thickness1)
        Element(9+i, [19+i, 21+i], thickness=thickness1)
        Element(11+i, [25+i, 27+i], thickness=thickness1)
        Element(13+i, [29+i, 31+i], thickness=thickness1)

    for i in range(2):
        Element.Arc(15+i, [3+i, 5+i], [m[i]*0.0336, 0.0924], thickness=thickness1)
        Element.Arc(17+i, [7+i, 9+i], [m[i]*0.0333, 0.0633], thickness=thickness1)
        Element.Arc(19+i, [11+i, 13+i], [m[i]*0.0672, 0.0607], thickness=thickness1)
        Element.Arc(21+i, [15+i, 17+i], [m[i]*0.068, 0.0276], thickness=thickness1)
        Element.Arc(23+i, [17+i, 19+i], [m[i]*0.065, 0.025], thickness=thickness1)
        Element.Arc(25+i, [21+i, 23+i], [m[i]*0.065, 0.012], thickness=thickness1)
        Element.Arc(27+i, [23+i, 25+i], [m[i]*0.068, 0.0094], thickness=thickness1)
        Element.Arc(29+i, [27+i, 29+i], [m[i]*0.0669, -0.0014], thickness=thickness1)
        Element.Arc(31+i, [31+i, 33+i], [m[i]*0.0047, -0.0027], thickness=thickness1)
    
    Element.Arc(33, [33, 34], [0, 0], thickness=thickness1)

    # Creating Part
    Part(1, '1-33')    

    Model.clientModel.service.finish_modification()

    Calculate_all()
