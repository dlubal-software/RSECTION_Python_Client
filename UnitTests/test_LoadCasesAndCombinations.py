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
from RSECTION.BasicObjects.point import Point
from RSECTION.BasicObjects.line import Line
from RSECTION.BasicObjects.part import Part
from RSECTION.BasicObjects.opening import Opening
from RSECTION.BasicObjects.element import Element
from RSECTION.LoadCasesAndCombinations.loadcase import LoadCase

if Model.clientModel is None:
    Model()

def test_stresspoint():

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

    LoadCase(1, ActionCategoryType.ACTION_CATEGORY_PERMANENT_G, True, 'Load Case 1')
    LoadCase(2, ActionCategoryType.ACTION_CATEGORY_PERMANENT_IMPOSED_GQ, True)

    Model.clientModel.service.finish_modification()

    lc_1 = Model.clientModel.service.get_load_case(1)
    lc_2 = Model.clientModel.service.get_load_case(2)

    assert lc_1.name == "Load Case 1"
    assert lc_2.action_category == "ACTION_CATEGORY_PERMANENT_IMPOSED_GQ"
