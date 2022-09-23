from RSECTION.initModel import Model, clearAtributes, ConvertStrToListOfInt
from RSECTION.enums import ObjectTypes

class Section():

    def __init__(self,
                 no: int = 1,
                 name: str = 'IPE 80',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Section Tag
            name (str): Section Name
            material_no (int): Material Number
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Section
        clientObject = model.clientModel.factory.create('ns0:section')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Section No.
        clientObject.no = no

        # Section nNme
        clientObject.name = name

        # Material No.
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Section to client model
        model.clientModel.service.set_section(clientObject)

    @staticmethod
    def DeleteSection(sections_no: str = '1 2', model = Model):

        '''
        Args:
            sections_no (str): Sections Number
            model (RSECTION Class, optional): Model to be edited

        '''

        # Delete from client model
        for section in ConvertStrToListOfInt(sections_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_SECTION.name, section)