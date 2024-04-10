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

def test_material():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Model.clientModel.service.finish_modification()

    material = Model.clientModel.service.get_material(1)
    assert material.no == 1
    assert material.name == 'S275 | CYS EN 1993-1-1:2009-03'

def test_section():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')
    Section(1, 'IPE 200')

    Model.clientModel.service.finish_modification()

    section = Model.clientModel.service.get_section(1)

    assert section.no == 1
    assert section.name == 'IPE 200 | -- | British Steel'

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
    assert Point_5.reference_type == "REFERENCE_TYPE_Y"

def test_line():

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
    Point(10, 0, -0.2)
    Point(11, 0.6, -0.2)

    Line(1, '1 2')
    Line.Polyline(2, '1 3')
    Line.Arc(3, [1, 3], [0.1,0.3], LineArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_ARC_CONTROL_POINT)
    Line.Circle(4, [-0.1, 0.0], 0.1)
    Line.Ellipse(5, [7 ,8], [-0.15,0.16])
    Line.Parabola(6, [1, 8], [-0.15,0.35], 0.1)
    Line.NURBS(7,'10 11', [[0,-0.2], [0.2,-0.3],[0.4,-0.1],[0.6,-0.2]], 3, [1,1,1,1])
    Line.NURBS(8,'10 11', [[0,-0.2], [0.2,-0.1],[0.4,-0.3],[0.6,-0.2]], 3)

    Model.clientModel.service.finish_modification()

    line_1 = Model.clientModel.service.get_line(1)
    line_2 = Model.clientModel.service.get_line(2)
    line_3 = Model.clientModel.service.get_line(3)
    line_4 = Model.clientModel.service.get_line(4)
    line_5 = Model.clientModel.service.get_line(5)
    line_6 = Model.clientModel.service.get_line(6)
    line_7 = Model.clientModel.service.get_line(7)
    line_8 = Model.clientModel.service.get_line(8)

    assert line_1.no == 1
    assert line_2.length == 0.2
    assert line_3.arc_first_point == 1
    assert line_4.circle_radius == 0.1
    assert line_5.ellipse_second_point == 8
    assert line_6.parabola_alpha == 0.1
    assert line_7.nurbs_control_points_by_components[0][1].row['weight'] == 1.0
    assert line_8.nurbs_order == 3

def test_part():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Part(1, '1 2 3 4')

    Model.clientModel.service.finish_modification()

    part = Model.clientModel.service.get_part(1)

    assert part.boundary_lines == "1 2 3 4"

def test_opening():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line.Circle(5, [0, 0], 0.5)

    Part(1, '1 2 3 4')
    Opening(1, '5')

    Model.clientModel.service.finish_modification()

    opening = Model.clientModel.service.get_opening(1)

    assert opening.boundary_lines == "5"

def test_element():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)
    Point(5,0.75,0.75)
    Point(6,0.75,-0.75)
    Point(7,-0.75,-0.75)
    Point(8,-0.75,0.75)
    Point(9, 0.75, 0)
    Point(10, 0, 0.75)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line.Circle(5, [0, 0], 0.5)

    Part(1, '1 2 3 4')

    Opening(1, '5')

    Element(1, '7 8', 0.5)
    Element.SingleLine(2, '6 7', 0.5, [True, 0.49])
    Element.Arc(3, [9, 10], [0.5303,0.5303], ElementArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC, 0.5)

    Model.clientModel.service.finish_modification()

    element_1 = Model.clientModel.service.get_element(1)
    element_2 = Model.clientModel.service.get_element(2)
    element_3 = Model.clientModel.service.get_element(3)

    assert element_1.thickness == 0.5
    assert element_2.effective_thickness == 0.49
    assert element_3.arc_first_point == 9

def test_elementcircle():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)
    Point(5,0.75,0.75)
    Point(6,0.75,-0.75)
    Point(7,-0.75,-0.75)
    Point(8,-0.75,0.75)
    Point(9, 0.75, 0)
    Point(10, 0, 0.75)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line.Circle(5, [0, 0], 0.5)

    Part(1, '1 2 3 4')

    Opening(1, '5')

    Element.Circle(1, [0,0], 0.75, 0.5)

    Model.clientModel.service.finish_modification()

    element_1 = Model.clientModel.service.get_element(1)

    assert element_1.circle_radius == 0.75

def test_elementellipse():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)
    Point(5,0.75,0.75)
    Point(6,0.75,-0.75)
    Point(7,-0.75,-0.75)
    Point(8,-0.75,0.75)
    Point(9, 0.75, 0)
    Point(10, 0, 0.75)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line.Circle(5, [0, 0], 0.5)

    Part(1, '1 2 3 4')

    Opening(1, '5')

    Element.Ellipse(1, [8, 6], [0.45, 0.45], 0.25)

    Model.clientModel.service.finish_modification()

    element_1 = Model.clientModel.service.get_element(1)

    assert element_1.ellipse_control_point_y == 0.45

def test_elementparabola():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)
    Point(5,0.75,0.75)
    Point(6,0.75,-0.75)
    Point(7,-0.75,-0.75)
    Point(8,-0.75,0.75)
    Point(9, 0.75, 0)
    Point(10, 0, 0.75)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line.Circle(5, [0, 0], 0.5)

    Part(1, '1 2 3 4')

    Opening(1, '5')

    Element.Parabola(1, [8, 6], [-0.6, -0.6], 0, 0.25)

    Model.clientModel.service.finish_modification()

    element_1 = Model.clientModel.service.get_element(1)

    assert element_1.parabola_second_point == 6

def test_elementnurbs():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S275')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)
    Point(5,0.75,0.75)
    Point(6,0.75,-0.75)
    Point(7,-0.75,-0.75)
    Point(8,-0.75,0.75)
    Point(9, 0.75, 0)
    Point(10, 0, 0.75)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line.Circle(5, [0, 0], 0.5)

    Part(1, '1 2 3 4')

    Opening(1, '5')

    Element.NURBS(1, '6 8', [[0.75,-0.75], [0.75, 0], [0, 0.75], [-0.75,0.75]], [1, 1, 1, 1], 3, 0.25)

    Model.clientModel.service.finish_modification()

    element_1 = Model.clientModel.service.get_element(1)

    assert element_1.nurbs_control_points_by_components[0][0].row['global_coordinate_z'] == -0.75
