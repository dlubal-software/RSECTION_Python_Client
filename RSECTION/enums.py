from enum import Enum


class ObjectTypes(Enum):
    '''
    Object Types
    '''

    E_OBJECT_TYPE_MATERIAL, E_OBJECT_TYPE_SECTION, E_OBJECT_TYPE_POINT, E_OBJECT_TYPE_LINE, \
    E_OBJECT_TYPE_PART, E_OBJECT_TYPE_OPENING, E_OBJECT_TYPE_ELEMENT = range(7)


class PointType(Enum):
    '''
    Point Type | Enumeration
    '''
    TYPE_STANDARD, TYPE_BETWEEN_TWO_POINTS, TYPE_BETWEEN_TWO_LOCATIONS, TYPE_ON_LINE = range(4)

class PointCoordinateSystemType(Enum):
    '''
    Point Coordinate System Type | Enum
    '''
    COORDINATE_SYSTEM_CARTESIAN = range(1)

class PointReferenceType(Enum):
    '''
    Point Reference Type| Enum
    '''
    REFERENCE_TYPE_L, REFERENCE_TYPE_Y, REFERENCE_TYPE_Z = range(3)

class LineType(Enum):
    '''
    Line Type | Enumeration
    '''
    TYPE_POLYLINE, TYPE_ARC, TYPE_CIRCLE, TYPE_ELLIPSE, TYPE_PARABOLA, TYPE_NURBS = range(6)

class LineArcAlphaAdjustmentTarget(Enum):
    '''
    Line Arc Alpha Adjustment Target | Enumeration
    '''
    ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC, ALPHA_ADJUSTMENT_TARGET_ARC_CONTROL_POINT, ALPHA_ADJUSTMENT_TARGET_END_OF_ARC = range(3)

class ElementType(Enum):
    '''
    Element Type | Enumeration
    '''
    TYPE_SINGLELINE, TYPE_ARC, TYPE_CIRCLE, TYPE_ELLIPSE, TYPE_PARABOLA, TYPE_NURBS = range(6)

class ElementArcAlphaAdjustmentTarget(Enum):
    '''
    Element Arc Alpha Adjustment Target | Enumeration
    '''
    ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC, ALPHA_ADJUSTMENT_TARGET_ARC_CONTROL_POINT, ALPHA_ADJUSTMENT_TARGET_END_OF_ARC = range(3)

class StressPointType(Enum):
    '''
    Element Type | Enumeration
    '''
    TYPE_STANDARD, TYPE_ON_LINE, TYPE_ON_ELEMENT = range(3)

class ElementSide(Enum):
    '''
    Element Side | Enumeration
    '''
    ELEMENT_SIDE_MIDDLE, ELEMENT_SIDE_LEFT, ELEMENT_SIDE_RIGHT = range(3)

class OptimizeOnType(Enum):
    '''
    Optimization Settings Optimize On Type | Enumeration
    '''
    E_OPTIMIZE_ON_TYPE_MIN_WHOLE_WEIGHT, E_OPTIMIZE_ON_TYPE_MIN_VECTORIAL_DISPLACEMENT, E_OPTIMIZE_ON_TYPE_MIN_MEMBER_DEFORMATION, \
    E_OPTIMIZE_ON_TYPE_MIN_SURFACE_DEFORMATION, E_OPTIMIZE_ON_TYPE_MIN_COST, E_OPTIMIZE_ON_TYPE_MIN_CO2_EMISSIONS = range(6)

class Optimizer(Enum):
    '''
    Optimization Settings Optimizer | Enumeration
    '''
    E_OPTIMIZER_TYPE_ALL_MUTATIONS, E_OPTIMIZER_TYPE_PERCENTS_OF_RANDOM_MUTATIONS, E_OPTIMIZER_TYPE_PARTICLE_SWARM = range(3)

