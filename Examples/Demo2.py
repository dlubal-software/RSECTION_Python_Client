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

if __name__ == '__main__':

    Model(True, "Demo2") # crete new model called Demo2

    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    m = [-1, -1, 1, 1, -1, -1, 1, 1]
    n = [1, -1, -1, 1, 1, -1, -1, 1,]

    for i in range(4):
        Point(i+1, m[i]*0.2, n[i]*0.2)
        Point(i+5, m[i]*0.16, n[i]*0.14)
        Point(i+9, m[i]*0.14, n[i]*0.16)
        Point(i+13, m[i]*0.175, n[i]*0.175)
        Point(i+17, m[i]*0.1282, n[i]*0.1282)

    Line.Circle(1, [0, 0], 0.15)
    Line.NURBS(2, '1 2', [[-0.2, 0.2],[-0.4, 0.14],[-0.6, 0],[-0.4,-0.14],[-0.2,-0.2]], [1,1,1,1,1,1], 3)
    Line.NURBS(3, '2 3', [[-0.2, -0.2],[-0.14, -0.4],[0, -0.6],[0.14,-0.4],[0.2,-0.2]], [1,1,1,1,1,1], 3)
    Line.NURBS(4, '3 4', [[0.2, -0.2],[0.4, -0.14],[0.6, 0],[0.4,0.14],[0.2,0.2]], [1,1,1,1,1,1], 3)
    Line.NURBS(5, '4 1', [[0.2, 0.2],[0.14, 0.4],[0, 0.6],[-0.14,0.4],[-0.2,0.2]], [1,1,1,1,1,1], 3)

    Model.clientModel.service.finish_modification()

    


