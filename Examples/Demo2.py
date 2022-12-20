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
from RSECTION.BasicObjects.opening import Opening
from RSECTION.BasicObjects.element import Element

if __name__ == '__main__':

    Model(True, "Demo2") # crete new model called Demo2

    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    m = [-1, -1, 1, 1]
    n = [1, -1, -1, 1]

    # Creating Points
    for i in range(4):
        Point(i+1, m[i]*0.2, n[i]*0.2)
        Point(i+5, m[i]*0.16, n[i]*0.14)
        Point(i+9, m[i]*0.14, n[i]*0.16)
        Point(i+13, m[i]*0.175, n[i]*0.175)
        Point(i+17, m[i]*0.1282, n[i]*0.1282)

    # Creating Lines 
    Line.Circle(1, [0, 0], 0.15)
    Line.NURBS(2, '1 2', [[-0.2,0.2],[-0.4,0.14],[-0.6,0],[-0.4,-0.14],[-0.2,-0.2]], 3)
    Line.NURBS(3, '2 3', [[-0.2,-0.2],[-0.14,-0.4],[0,-0.6],[0.14,-0.4],[0.2,-0.2]], 3)
    Line.NURBS(4, '3 4', [[0.2,-0.2],[0.4,-0.14],[0.6,0],[0.4,0.14],[0.2,0.2]], 3)
    Line.NURBS(5, '4 1', [[0.2,0.2],[0.14,0.4],[0,0.6],[-0.14,0.4],[-0.2,0.2]], 3)
    Line.NURBS(6, '5 6', [[-0.16,0.14],[-0.34,0.1],[-0.48,0],[-0.34,-0.1],[-0.16,-0.14]], 3)
    Line.NURBS(7, '10 11', [[-0.14,-0.16],[-0.1,-0.34],[0,-0.48],[0.1,-0.34],[0.14,-0.16]], 3)
    Line.NURBS(8, '7 8', [[0.16,-0.14],[0.34,-0.1],[0.48,0],[0.34,0.1],[0.16,0.14]], 3)
    Line.NURBS(9, '12 9', [[0.14,0.16],[0.1,0.34],[0,0.48],[-0.1,0.34],[-0.14,0.16]], 3)
    Line.Arc(10, [5, 6], [-0.2126,0])
    Line.Arc(11, [10, 11], [0,-0.2126])
    Line.Arc(12, [7, 8], [0.2126,0])
    Line.Arc(13, [12, 9], [0,0.2126])

    # Creating Part
    Part(1, '2 3 4 5')

    # Creating Openings
    Opening(1, '1')
    Opening(2, '6 10')
    Opening(3, '7 11')
    Opening(4, '8 12')
    Opening(5, '9 13')

    # Creating Elements
    Element.NURBS(1, '13 14', [[-0.175,0.175],[-0.37,0.12],[-0.53,0],[-0.37,-0.12],[-0.175,-0.175]], [1,1,1,1,1], 3, 0.055)
    Element.NURBS(2, '14 15', [[-0.175,-0.175],[-0.12,-0.37],[0,-0.53],[0.12,-0.37],[0.175,-0.175]], [1,1,1,1,1], 3, 0.055)
    Element.NURBS(3, '15 16', [[0.175,-0.175],[0.37,-0.12],[0.53,0],[0.37,0.12],[0.175,0.175]], [1,1,1,1,1], 3, 0.055)
    Element.NURBS(4, '16 13', [[0.175,0.175],[0.12,0.37],[0,0.53],[-0.12,0.37],[-0.175,0.175]], [1,1,1,1,1], 3, 0.055)
    Element.Circle(5, [0,0], 0.1813, 0.0626, circle_point=[-0.1282,-0.1282])
    
    Model.clientModel.service.finish_modification()

    #Calculate_all


