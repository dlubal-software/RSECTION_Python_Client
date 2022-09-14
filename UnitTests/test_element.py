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
