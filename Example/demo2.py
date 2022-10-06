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
from RSECTION.BasicObjects.section import Section
from RSECTION.BasicObjects.point import Point
from RSECTION.BasicObjects.line import Line
from RSECTION.BasicObjects.part import Part
from RSECTION.BasicObjects.opening import Opening
from RSECTION.BasicObjects.element import Element
from RSECTION.BasicObjects.stresspoint import StressPoint
from RSECTION.enums import *

if __name__ == '__main__':

    Model(True, "demo2") # crete new model called Demo

    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    Point(1, 0, 0)
    Point.Standard(2, 1, [0.1, 0.1])
    Point.Standard(3, 2, [-0.2, 0])
    Point.Standard(4, 3, [0, -0.2])
    Point.Standard(5, 4, [0.2, 0])
    Point(6, 0.07, 0.08)
    Point.Standard(7, 6, [-0.05, 0])
    Point.Standard(8, 7, [-0.01, -0.01])
    Point.Standard(9, 8, [0, -0.05])
    Point.Standard(10, 9, [0.01, -0.01])
    Point.Standard(11, 10, [0.05, 0])
    Point.Standard(12, 11, [0.01, 0.01])
    Point.Standard(13, 12, [0, 0.05])
    Point(14, -0.02, 0.08)
    Point.Standard(15, 14, [-0.05, 0])
    Point.Standard(16, 15, [-0.01, -0.01])
    Point.Standard(17, 16, [0, -0.05])
    Point.Standard(18, 17, [0.01, -0.01])
    Point.Standard(19, 18, [0.05, 0])
    Point.Standard(20, 19, [0.01, 0.01])
    Point.Standard(21, 20, [0, 0.05])
    Point(22, -0.02, -0.01)
    Point.Standard(23, 22, [-0.05, 0])
    Point.Standard(24, 23, [-0.01, -0.01])
    Point.Standard(25, 24, [0, -0.05])
    Point.Standard(26, 25, [0.01, -0.01])
    Point.Standard(27, 26, [0.05, 0])
    Point.Standard(28, 27, [0.01, 0.01])
    Point.Standard(29, 28, [0, 0.05])
    Point(30, 0.07, -0.01)
    Point.Standard(31, 30, [-0.05, 0])
    Point.Standard(32, 31, [-0.01, -0.01])
    Point.Standard(33, 32, [0, -0.05])
    Point.Standard(34, 33, [0.01, -0.01])
    Point.Standard(35, 34, [0.05, 0])
    Point.Standard(36, 35, [0.01, 0.01])
    Point.Standard(37, 36, [0, 0.05])

    Point(38, 0.09, 0.09)
    Point(39, -0.09, 0.09)
    Point(40, -0.09, -0.09)
    Point(41, 0.09, -0.09)
    Point.BetweenTwoPoints(42, 38, 39, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], 0)
    Point.BetweenTwoPoints(43, 39, 40, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], 0)
    Point.BetweenTwoPoints(44, 40, 41, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], 0)
    Point.BetweenTwoPoints(45, 41, 38, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], 0)

    Line(1, '2 3')
    Line(2, '3 4')
    Line(3, '4 5')
    Line(4, '5 2')
    
    Line(5, '6 7')
    Line.Arc(6, [7, 8], [0.0129, 0.0771])
    Line(7, '8 9')
    Line.Arc(8, [9, 10], [0.0129, 0.0129])
    Line(9, '10 11')
    Line.Arc(10, [11, 12], [0.0771, 0.0129])
    Line(11, '12 13')
    Line.Arc(12, [13, 6], [0.0771, 0.0771])

    Line(13, '14 15')
    Line.Arc(14, [15, 16], [-0.0771, 0.0771])
    Line(15, '16 17')
    Line.Arc(16, [17, 18], [-0.0771, 0.0129])
    Line(17, '18 19')
    Line.Arc(18, [19, 20], [-0.0129, 0.0129])
    Line(19, '20 21')
    Line.Arc(20, [21, 14], [-0.0129, 0.0771])

    Line(21, '22 23')
    Line.Arc(22, [23, 24], [-0.0771, -0.0129])
    Line(23, '24 25')
    Line.Arc(24, [25, 26], [-0.0771, -0.0771])
    Line(25, '26 27')
    Line.Arc(26, [27, 28], [-0.0129, -0.0771])
    Line(27, '28 29')
    Line.Arc(28, [29, 22], [-0.0129, -0.0129])

    Line(29, '30 31')
    Line.Arc(30, [31, 32], [0.0129, -0.0129])
    Line(31, '32 33')
    Line.Arc(32, [33, 34], [0.0129, -0.0771])
    Line(33, '34 35')
    Line.Arc(34, [35, 36], [0.0771, -0.0771])
    Line(35, '36 37')
    Line.Arc(36, [37, 30], [0.0771, -0.0129])

    Part(1, '1 2 3 4')

    Opening(1, '5 6 7 8 9 10 11 12')
    Opening(2, '13 14 15 16 17 18 19 20')
    Opening(3, '21 22 23 24 25 26 27 28')
    Opening(4, '29 30 31 32 33 34 35 36')

    Element(1, '38 42', 0.02)
    Element(2, '42 39', 0.02)
    Element(3, '39 43', 0.02)
    Element(4, '43 40', 0.02)
    Element(5, '40 44', 0.02)
    Element(6, '44 41', 0.02)
    Element(7, '41 45', 0.02)
    Element(8, '45 38', 0.02)
    Element(9, '42 1', 0.02)
    Element(10, '43 1', 0.02)
    Element(11, '44 1', 0.02)
    Element(12, '45 1', 0.02)

    Model.clientModel.service.finish_modification()

    Calculate_all()
