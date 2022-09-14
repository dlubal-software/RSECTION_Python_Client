import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RSECTION.enums import *
from RSECTION.initModel import Model
from RSECTION.BasicObjects.material import Material
from RSECTION.BasicObjects.section import Section
from RSECTION.BasicObjects.point import Point
from RSECTION.BasicObjects.line import Line
from RSECTION.BasicObjects.part import Part
from RSECTION.BasicObjects.opening import Opening
from RSECTION.BasicObjects.element import Element

if Model.clientModel is None:
    Model()

def test_point():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Point(1, 0.0, 0.2)
    Point(2, 0.2, 0,0)
    Point.Standard(3, 2, [0.0,0.2])
    Point.BetweenTwoPoints(4, 1, 2, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], -0.1)
    Point.BetweenTwoPoints(5, 1, 3, PointReferenceType.REFERENCE_TYPE_Y, [False, 0.08], -0.1)
    Point.BetweenTwoPoints(6, 1, 3, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], 0.1)
    Point.BetweenTwoLocations(7, 0.0, 0.0, -0.2, 0.4, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], 0.0)
    Point.BetweenTwoLocations(8, -0.2, 0.0, 0.0, 0.4, PointReferenceType.REFERENCE_TYPE_Z, [False, 0.2], -0.1)
    Line(1, '1 2')
    Point.OnLine(9, 1, PointReferenceType.REFERENCE_TYPE_Y, [False, 0.1])

    Model.clientModel.service.finish_modification()

    Point_1 = Model.clientModel.service.get_point(1)
    Point_2 = Model.clientModel.service.get_point(3)
    Point_3 = Model.clientModel.service.get_point(4)
    Point_4 = Model.clientModel.service.get_point(7)
    Point_5 = Model.clientModel.service.get_point(9)

    assert Point_1.coordinate_2 == 0.2
    assert Point_2.reference_point == 2
    assert Point_3.distance_from_start_relative == 0.5
    assert Point_4.reference_type == "REFERENCE_TYPE_L"
    assert Point_5.on_line_reference_line == 1
