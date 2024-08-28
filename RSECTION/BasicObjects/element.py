from RSECTION.initModel import Model, clearAtributes, ConvertToDlString, ConvertStrToListOfInt
from RSECTION.enums import ElementType, ElementArcAlphaAdjustmentTarget, ObjectTypes

class Element():

    def __init__(self,
                 no: int = 1,
                 points_no: str = '1 2',
                 thickness: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Element Tag
            points_no (str): Points Number
            thickness (float): Element Thickness
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Points No.
        clientObject.definition_points = ConvertToDlString(points_no)

        # Element Thickness

        clientObject.thickness = thickness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)

    @staticmethod
    def SingleLine(
                   no: int = 1,
                   points_no: str = '1 2',
                   thickness: float = 0.0,
                   effective_thickness: list = [False, None],
                   comment: str = '',
                   params: dict = None,
                   model = Model):

        '''
        Args:
            no (int): Element Tag
            points_no (str): Points Number
            thickness (float): Element Thickness
            effective_thickness (list): Effective Thickness List
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Points No.
        clientObject.definition_points = ConvertToDlString(points_no)

        # Element Type
        clientObject.type = ElementType.TYPE_SINGLELINE.name

        # Element Thickness
        clientObject.thickness = thickness

        # Effective Thickness

        if effective_thickness[0] == True:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        else:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)

    @staticmethod
    def Arc(
            no: int = 1,
            points_no: list = [1, 2],
            control_point: list = None,
            alpha_adjustment_target = ElementArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC,
            thickness: float = 0.0,
            effective_thickness: list = [False, None],
            comment: str = '',
            params: dict = None,
            model = Model):

        '''
        Args:
            no (int): Element Tag
            points_no (list): Points Number
            control_point (list): Control Point coordinate for Arc in [Y, Z]
            alpha_adjustment_target (enum): Element Arc Alpha Adjustment Target Enumeration
            thickness (float): Element Thickness
            effective_thickness (list): Effective Thickness List
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = ElementType.TYPE_ARC.name

        # Points No. and Control Point Coordinates
        clientObject.arc_first_point = points_no[0]
        clientObject.arc_second_point = points_no[1]
        clientObject.arc_alpha_adjustment_target = alpha_adjustment_target.name
        clientObject.arc_control_point_y = control_point[0]
        clientObject.arc_control_point_z = control_point[1]

        # Element Thickness
        clientObject.thickness = thickness

        # Effective Thickness

        if effective_thickness[0] == True:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        else:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)

    @staticmethod
    def Circle(
                no: int = 1,
                center_of_cirle: list = [0.0, 0.0],
                circle_radius: float = 0.1,
                thickness: float = 0.0,
                effective_thickness: list = [False, None],
                comment: str = '',
                params: dict = None,
                model = Model):

        '''
        Args:
            no (int): Element Tag
            center_of_cirle (list): Coordinate of Circle Center
            circle_radius (float): Circle Radius
            thickness (float): Element Thickness
            effective_thickness (list): Effective Thickness List
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = ElementType.TYPE_CIRCLE.name

        # Center of circle and Radius
        clientObject.circle_center_coordinate_y = center_of_cirle[0]
        clientObject.circle_center_coordinate_z = center_of_cirle[1]

        clientObject.circle_radius = circle_radius

        # Element Thickness
        clientObject.thickness = thickness

        # Effective Thickness

        if effective_thickness[0] == True:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        else:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)

    @staticmethod
    def Ellipse(
                no: int = 1,
                points_no: list = [1, 2],
                control_point: list = None,
                thickness: float = 0.0,
                effective_thickness: list = [False, None],
                comment: str = '',
                params: dict = None,
                model = Model):

        '''
        Args:
            no (int): Element Tag
            points_no (list): Points Number
            control_point (list): Control Point coordinate for Ellipse in [Y, Z]
            thickness (float): Element Thickness
            effective_thickness (list): Effective Thickness List
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = ElementType.TYPE_ELLIPSE.name

        # Points No. and Ellipse Control Point Coordinates
        clientObject.ellipse_first_point = points_no[0]
        clientObject.ellipse_second_point = points_no[1]
        clientObject.ellipse_control_point_y = control_point[0]
        clientObject.ellipse_control_point_z = control_point[1]

        # Element Thickness
        clientObject.thickness = thickness

        # Effective Thickness

        if effective_thickness[0] == True:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        else:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)

    @staticmethod
    def Parabola(
                 no: int = 1,
                 points_no: list = [1, 2],
                 control_point: list = None,
                 alpha: float = 0.0,
                 thickness: float = 0.0,
                 effective_thickness: list = [False, None],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Element Tag
            points_no (list): Points Number
            control_point (list): Control Point coordinate for Parabola in [Y, Z]
            alpha (float): Alpha Angle (in Radians)
            thickness (float): Element Thickness
            effective_thickness (list): Effective Thickness List
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = ElementType.TYPE_PARABOLA.name

        # Points No. and Parabola Control Point Coordinates
        clientObject.parabola_first_point = points_no[0]
        clientObject.parabola_second_point = points_no[1]
        clientObject.parabola_control_point_y = control_point[0]
        clientObject.parabola_control_point_z = control_point[1]

        clientObject.parabola_alpha = alpha

        # Element Thickness
        clientObject.thickness = thickness

        # Effective Thickness

        if effective_thickness[0] == True:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        else:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)

    @staticmethod
    def NURBS(
              no: int = 1,
              control_points: str = None,
              components: list = None,
              weights: list = None,
              order: int = None,
              thickness: float = 0.0,
              effective_thickness: list = [False, None],
              comment: str = '',
              params: dict = None,
              model = Model):

        '''
        Args:
            no (int): Element Tag
            control_points (str): String of Start Point and End Point (example: '1 2')
            components (list of lists): Control Points List
                component = [[start_point_x, start_point_y],
                             [control_point_x, control_point_y],
                             ....,
                             [end_point_x, end_point_y]]
            weights (list): Control Points Weights
            order (int): Nurbs Order
            thickness (float): Element Thickness
            effective_thickness (list): Effective Thickness List
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = ElementType.TYPE_NURBS.name

        # Control points
        clientObject.definition_points = ConvertToDlString(control_points)

        # Nurbs Order
        if order > 1 and order <= len(components):
            clientObject.nurbs_order = order
        else:
            print('Error: Please write Nurbs order in range 2 and number of Control Points!')

        #Local Section Reduction Components
        clientObject.nurbs_control_points_by_components = model.clientModel.factory.create('ns0:array_of_element_nurbs_control_points_by_components')

        for i,j in enumerate(components):
            nurbs = model.clientModel.factory.create('ns0:element_nurbs_control_points_by_components_row')
            nurbs.no = i+1
            nurbs.row.global_coordinate_y = components[i][0]
            nurbs.row.global_coordinate_z = components[i][1]
            nurbs.row.weight = weights[i]

            clientObject.nurbs_control_points_by_components.element_nurbs_control_points_by_components.append(nurbs)

        # Element Thickness
        clientObject.thickness = thickness

        # Effective Thickness

        if effective_thickness[0] == True:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        else:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)

    @staticmethod
    def DeleteElement(elements_no: str = '1 2', model = Model):

        '''
        Args:
            elements_no (str): Elements Number
            model (RSECTION Class, optional): Model to be edited
        '''

        # Delete from client model
        for element in ConvertStrToListOfInt(elements_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_ELEMENT.name, element)
