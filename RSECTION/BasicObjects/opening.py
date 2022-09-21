from RSECTION.initModel import Model, clearAtributes, ConvertToDlString, ConvertStrToListOfInt
from RSECTION.enums import ObjectTypes

class Opening():

    def __init__(self,
                 no: int = 1,
                 boundary_lines: str = '1 2 3 4',
                 part_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Opening Tag
            boundary_lines (str): Boundary Lines Number
            part_no (int): Part Number
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Opening
        clientObject = model.clientModel.factory.create('ns0:opening')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Opening No.
        clientObject.no = no

        # Boundary Lines No.
        clientObject.boundary_lines = ConvertToDlString(boundary_lines)

        # Assign to Part

        clientObject.parts = part_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Opening to client model
        model.clientModel.service.set_opening(clientObject)

    @staticmethod
    def DeleteOpening(openings_no: str = '1 2', model = Model):

        '''
        Args:
            openings_no (str): Openings Number
            model (RSECTION Class, optional): Model to be edited
        '''

        # Delete from client model
        for opening in ConvertStrToListOfInt(openings_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_OPENING.name, opening)
