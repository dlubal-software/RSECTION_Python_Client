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
from RSECTION.enums import PointReferenceType

if __name__ == '__main__':

    # User Defined Section Width and Hight
    h = float(input('Height of Section in m: '))
    b = float(input('Width of Section in m: '))
    
    # User Defined Modelname
    filename = str(input('Section modelname: '))
    if '.rsc' not in filename:
        filename = filename + '.rsc'
    
    # User Defined Filepath
    save = str(input('Do you want to save the file? [y/n]: '))
    if save.lower() == 'y':
        filepath = str(input('Filepath: '))

    # Create New Model
    Model(True, filename) 
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Creating Material
    Material(1, 'S235')

    # Creating Points
    n = [1, 1, -1, -1]
    m = [-1, 1, -1, 1]

    t = 0.003/2 # thickness of section is 3.0 mm
    for i in range(4):
        Point(i+36, m[i]*((b/2-t)-(b/2-t)*(73/137) + 0.011), (h-0.0045-t)+t*n[i])
        Point(i+40, m[i]*((b/2-t)-(b/2-t)*(73/137) + 0.0055), (h-0.0045-t)+t*n[i])
        Point(i+44, m[i]*((b/2-t)-(b/2-t)*(73/137)+t*n[i]), h-0.0045-0.007)
        Point(i+48, m[i]*((b/2-t)-(b/2-t)*(73/137)+t*n[i]), ((h-2*t)*66.5/97)-0.0045+0.003+t)
        Point(i+52, m[i]*((b/2-t)-(b/2-t)*(73/137)+0.0045), ((h-2*t)*66.5/97)-0.0045+t*n[i])
        Point(i+56, m[i]*(b/2-0.006), ((h-2*t)*66.5/97)-0.0045+t*n[i])
        Point(i+60, m[i]*((b/2-0.0015)+t*n[i]), ((h-2*t)*66.5/97)-0.0045-0.003-t)
        Point(i+64, m[i]*((b/2-0.0015)+t*n[i]), 0.0295)
        Point(i+74, m[i]*((b/2-0.0055)+t*n[i]), 0.0232)
        Point(i+78, m[i]*((b/2-0.0055)+t*n[i]), 0.0138)
        Point(i+90, m[i]*((b/2-0.0015)+t*n[i]), 0.0075)
        Point(i+94, m[i]*((b/2-0.0015)+t*n[i]), 0.0025)
        Point(i+98, m[i]*(b/2-0.007), -(0.003+t*n[i]))
        Point(i+102, m[i]*0.0061, -(0.003+t*n[i]))

    # Creating Points between to locations to determine intersection
    for i in range(2):
        Point.BetweenTwoLocations(82+i, m[i]*(b/2 - 0.005), 0.0075, m[i]*(b/2-0.002), 0.0138, PointReferenceType.REFERENCE_TYPE_L, [True, 5/7])
        Point.BetweenTwoLocations(86+i, m[i]*(b/2 - 0.005), 0.0075, m[i]*(b/2-0.002), 0.0138, PointReferenceType.REFERENCE_TYPE_L, [True, 2/7])
        Point.BetweenTwoLocations(68+i, m[i]*(b/2 - 0.005), 0.0295, m[i]*(b/2-0.002), 0.0232, PointReferenceType.REFERENCE_TYPE_L, [True, 2/7])
        Point.BetweenTwoLocations(72+i, m[i]*(b/2 - 0.005), 0.0295, m[i]*(b/2-0.002), 0.0232, PointReferenceType.REFERENCE_TYPE_L, [True, 5/7])
        Point.BetweenTwoLocations(106+i, m[i]*0.0061, 0.0002, 0, -0.0045, PointReferenceType.REFERENCE_TYPE_L, [True, 4.7/7.7])
        Point.BetweenTwoLocations(110+i, m[i]*0.0061, 0.0002, 0, -0.0045, PointReferenceType.REFERENCE_TYPE_L, [True, 1.7/7.7])
        
    Point(112, 0, 0+t)
    Point(113, 0, 0-t)

    # Creating Straight Lines   
    Line(67, '36 38')
    Line(68, '37 39')
 
    for i in range(4):
        Line(i+1, str(i+36)+' '+ str(i+40))
        Line(i+5, str(i+44)+' '+ str(i+48))
        Line(i+9, str(i+52)+' '+ str(i+56))
        Line(i+13, str(i+60)+' '+ str(i+64))
        Line(i+17, str(i+74)+' '+ str(i+78))
        Line(i+21, str(i+90)+' '+ str(i+94))
        Line(i+25, str(i+98)+' '+ str(i+102))

    # Creating Lines As Curves
    for i in range(2):
        Line.Arc(29+i, [40+i, 46+i], [m[i]*(((b/2-t)-(b/2-t)*(73/137)) + 0.0005503), h-0.0065503])
        Line.Arc(31+i, [50+i, 54+i], [m[i]*(((b/2-t)-(b/2-t)*(73/137)) + 0.0002574), ((h-t*2)*66.5/97)-0.0045+0.0002574])
        Line.Arc(33+i, [58+i, 62+i], [m[i]*(b/2-0.0038787), ((h-t*2)*66.5/97)-0.0045-t-0.0008787])
        Line.Arc(35+i, [66+i, 68+i], [m[i]*(b/2-0.0033093), 0.0284289])
        Line.Arc(37+i, [68+i, 76+i], [m[i]*(b/2-0.0062249), 0.0258467])
        Line.Arc(39+i, [80+i, 86+i], [m[i]*(b/2-0.0062249), 0.0111533])
        Line.Arc(41+i, [86+i, 92+i], [m[i]*(b/2-0.0033093), 0.0085711])
        Line.Arc(43+i, [96+i, 100+i], [m[i]*(b/2-0.0041716), -0.00032840])
        Line.Arc(45+i, [104+i, 110+i], [m[i]*0.0054, -0.0013])

    for i in range(2):
        Line.Arc(47+i, [42+i, 44+i], [m[i]*((b/2-t)-(b/2-t)*(73/137) + 0.0026716), h-0.0086716])
        Line.Arc(49+i, [48+i, 52+i], [m[i]*((b/2-t)-(b/2-t)*(73/137) + 0.0023787), (h-t*2)*66.5/97-0.0045+0.0023787])
        Line.Arc(51+i, [56+i, 60+i], [m[i]*(b/2-0.0017574), ((h-t*2)*66.5/97)-0.0045-0.0002574])
        Line.Arc(53+i, [64+i, 72+i], [m[i]*(b/2-0.0007732), 0.0268263])
        Line.Arc(55+i, [72+i, 74+i], [m[i]*(b/2-0.00369), 0.0242423])
        Line.Arc(57+i, [78+i, 82+i], [m[i]*(b/2-0.00369), 0.0127577])
        Line.Arc(59+i, [82+i, 90+i], [m[i]*(b/2-0.0007732), 0.0101737])  
        Line.Arc(61+i, [94+i, 98+i], [m[i]*((b/2-0.007)+0.0049497), -0.0024497])
        Line.Arc(63+i, [102+i, 106+i], [m[i]*0.004, -0.004])

    Line.Arc(65, [110, 111], [0, 0.0015])
    Line.Arc(66, [106, 107], [0, -0.0015])

    # Creating Part
    Part(1, '1-68')    

    Model.clientModel.service.finish_modification()

    Calculate_all()
    
    # Saving Model
    if save.lower() == 'y':
        model_path = os.path.join(filepath, filename)
        Model.clientModel.service.save(model_path)
