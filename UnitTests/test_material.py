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
