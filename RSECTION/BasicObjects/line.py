from RSECTION.initModel import Model, clearAtributes, ConvertToDlString, ConvertStrToListOfInt
from RSECTION.enums import LineType, LineArcAlphaAdjustmentTarget, ObjectTypes


class Line():

    def __init__(self,
                 no: int = 1,
                 points_no: str = '1 2',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Points No.
        clientObject.definition_points = ConvertToDlString(points_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def Polyline(
                 no: int = 1,
                 points_no: str = '1 2',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_POLYLINE.name

        # Points No.
        clientObject.definition_points = ConvertToDlString(points_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def Arc(
            no: int = 1,
            points_no: list = [1, 2],
            control_point: list = None,
            alpha_adjustment_target = LineArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC,
            comment: str = '',
            params: dict = None,
            model = Model):

        '''
        Args:
            control_point (list): Control Point coordinate for Arc in [Y, Z]

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_ARC.name

        # Points No. and Control Point Coordinates
        clientObject.arc_first_point = points_no[0]
        clientObject.arc_second_point = points_no[1]
        clientObject.arc_alpha_adjustment_target = alpha_adjustment_target.name
        clientObject.arc_control_point_y = control_point[0]
        clientObject.arc_control_point_z = control_point[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def Circle(
               no: int = 1,
               center_of_cirle: list = [0.0, 0.0],
               circle_radius: float = 0.1,
               comment: str = '',
               params: dict = None,
               model = Model):

        '''
        Args:

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_CIRCLE.name

        # Center of circle and Radius
        clientObject.circle_center_coordinate_y = center_of_cirle[0]
        clientObject.circle_center_coordinate_z = center_of_cirle[1]

        clientObject.circle_radius = circle_radius

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def Ellipse(
                no: int = 1,
                points_no: list = [1, 2],
                control_point: list = None,
                comment: str = '',
                params: dict = None,
                model = Model):

        '''
        Args:
            control_point (list): Control Point coordinate for Ellipse in [Y, Z]

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_ELLIPSE.name

        # Points No. and Ellipse Control Point Coordinates
        clientObject.ellipse_first_point = points_no[0]
        clientObject.ellipse_second_point = points_no[1]
        clientObject.ellipse_control_point_y = control_point[0]
        clientObject.ellipse_control_point_z = control_point[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def Parabola(
                 no: int = 1,
                 points_no: list = [1, 2],
                 control_point: list = None,
                 alpha: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            control_point (list): Control Point coordinate for Parabola in [Y, Z]
            alpha (float): Alpha Angle (in Radians)

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_PARABOLA.name

        # Points No. and Parabola Control Point Coordinates
        clientObject.parabola_first_point = points_no[0]
        clientObject.parabola_second_point = points_no[1]
        clientObject.parabola_control_point_y = control_point[0]
        clientObject.parabola_control_point_z = control_point[1]

        clientObject.parabola_alpha = alpha

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def NURBS(
              no: int = 1,
              control_points: str = None,
              components: list = None,
              weights: list = None,
              order: int = None,
              comment: str = '',
              params: dict = None,
              model = Model):

        '''
        Args:
            control_points (str): String of Start Point and End Point (example: '1 2')
            components (list of lists): Control Points List
                component = [[start_point_x, start_point_y],
                             [control_point_x, control_point_y],
                             ....,
                             [end_point_x, end_point]]
            weights (list): Control Points Weights

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_NURBS.name

        # Control points
        clientObject.definition_points = ConvertToDlString(control_points)

        # Nurbs Order
        if order > 1 and order <= len(components):
            clientObject.nurbs_order = order
        else:
            print('Error: Please write Nurbs order in range 2 and number of Control Points!')

        #Local Section Reduction Components
        clientObject.nurbs_control_points_by_components = model.clientModel.factory.create('ns0:array_of_line_nurbs_control_points_by_components')

        for i,j in enumerate(components):
            nurbs = model.clientModel.factory.create('ns0:line_nurbs_control_points_by_components_row')
            nurbs.no = i+1
            nurbs.row.global_coordinate_y = components[i][0]
            nurbs.row.global_coordinate_z = components[i][1]
            nurbs.row.weight = weights[i]

            clientObject.nurbs_control_points_by_components.line_nurbs_control_points_by_components.append(nurbs)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def DeleteLine(lines_no: str = '1 2', model = Model):

        '''
        Args:

        '''

        # Delete from client model
        for line in ConvertStrToListOfInt(lines_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_LINE.name, line)


