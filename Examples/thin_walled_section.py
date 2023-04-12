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

    Model(True, "Steelracksystem.rsc") # crete new model called Steelracksystem

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
    n = [1, 1, -1, -1]
    for i in range(4):
        Point(i+36, m[i]*0.043, 0.094+t*n[i])
        Point(i+40, m[i]*0.0375, 0.094+t*n[i])
        Point(i+44, m[i]*(0.032+t*n[i]), 0.0885)
        Point(i+48, m[i]*(0.032+t*n[i]), 0.0665)
        Point(i+52, m[i]*0.0365, 0.062+t*n[i])
        Point(i+56, m[i]*0.064, 0.062+t*n[i])
        Point(i+60, m[i]*(0.0685+t*n[i]),0.0575)
        Point(i+64, m[i]*(0.0685+t*n[i]), 0.0295)
        Point(68, m[i]*-0.0659, 0.0277)
        Point(69, m[i]*0.0659, 0.0277)
        Point(72, m[i]*-0.0671, 0.0249)
        Point(73, m[i]*0.0671, 0.0249)
        Point(i+74, m[i]*(0.0645+t*n[i]), 0.0232)
        Point(i+78, m[i]*(0.0645+t*n[i]), 0.0138)
        Point(82, m[i]*-0.0671, 0.0121)
        Point(83, m[i]*0.0671, 0.0121)
        Point(86, m[i]*-0.0659, 0.0093)
        Point(87, m[i]*0.0659, 0.0093)
        Point(i+90, m[i]*(0.0685+t*n[i]), 0.0075)
        Point(i+94, m[i]*(0.0685+t*n[i]), 0.0025)
        Point(i+98, m[i]*0.063, -(0.003+t*n[i]))
        Point(i+102, m[i]*0.0061, -(0.003+t*n[i]))
        Point(106, m[i]*-0.0024, -0.0027)
        Point(107, m[i]*0.0024, -0.0027)
        Point(110, m[i]*-0.0048, -0.0007)
        Point(111, m[i]*0.0048, -0.0007)
        
    Point(112, 0, 0+t)
    Point(113, 0, 0-t)

    Line(67, '36 38')
    Line(68, '37 39')
    # Creating Lines     
    for i in range(4):
        Line(i+1, str(i+36)+' '+ str(i+40))
        Line(i+5, str(i+44)+' '+ str(i+48))
        Line(i+9, str(i+52)+' '+ str(i+56))
        Line(i+13, str(i+60)+' '+ str(i+64))
        Line(i+17, str(i+74)+' '+ str(i+78))
        Line(i+21, str(i+90)+' '+ str(i+94))
        Line(i+25, str(i+98)+' '+ str(i+102))

    s = 0.001
    for i in range(2):
        Line.Arc(29+i, [40+i, 46+i], [m[i]*(0.0336-s), 0.0924+s])
        Line.Arc(31+i, [50+i, 54+i], [m[i]*(0.0333-s), 0.0633-s])
        Line.Arc(33+i, [56+i, 60+i], [m[i]*(0.0672+s), 0.0607+s])
        Line.Arc(35+i, [66+i, 68+i], [m[i]*0.0667, 0.0284])
        Line.Arc(37+i, [68+i, 76+i], [m[i]*0.0638, 0.0258])
        Line.Arc(39+i, [80+i, 86+i], [m[i]*0.0638, 0.0112])
        Line.Arc(41+i, [86+i, 92+i], [m[i]*0.0667, 0.0086])
        Line.Arc(43+i, [94+i, 98+i], [m[i]*(0.0669+s), -(0.0014+s)])
        Line.Arc(45+i, [104+i, 110+i], [m[i]*0.0054, -0.0013])
    
    k = 0.0011
    for i in range(2):
        Line.Arc(47+i, [42+i, 44+i], [m[i]*(0.0336+k), 0.0924-k])
        Line.Arc(49+i, [48+i, 52+i], [m[i]*(0.0333+k), 0.0633+k])
        Line.Arc(51+i, [58+i, 62+i], [m[i]*(0.0672-k), 0.0607-k])
        Line.Arc(53+i, [64+i, 72+i], [m[i]*0.0692, 0.0268])
        Line.Arc(55+i, [72+i, 74+i], [m[i]*0.0663, 0.0243])
        Line.Arc(57+i, [78+i, 82+i], [m[i]*0.0663, 0.0128])
        Line.Arc(59+i, [82+i, 90+i], [m[i]*0.0692, 0.0102])
        Line.Arc(61+i, [96+i, 100+i], [m[i]*(0.0669-k), -(0.0014-k)])
        Line.Arc(63+i, [102+i, 106+i], [m[i]*0.004, -0.004])

    Line.Arc(65, [110, 111], [0, 0.0015])
    Line.Arc(66, [106, 107], [0, -0.0015])


    thickness1 = 0.003
    # Creating Elements
    for i in range(2):
        Element(1+i, [1+i, 3+i], thickness=thickness1)
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
    Part(1, '1-68')    

    Model.clientModel.service.finish_modification()

    Calculate_all()
