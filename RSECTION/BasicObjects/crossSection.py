from RSECTION.initModel import Model, clearAttributes, ConvertStrToListOfInt
from RSECTION.enums import ObjectTypes

class CrossSection():

    def __init__(self,
                 no: int = 1,
                 name: str = 'IPE 80',
                 material_no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Cross Section Tag
            name (str): Cross Section Name
            material_no (int): Material Number
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Cross Section
        clientObject = model.clientModel.factory.create('ns0:cross_section')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Cross Section No.
        clientObject.no = no

        # Cross Section nNme
        clientObject.name = name

        # Material No.
        clientObject.material = material_no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add CrossSection to client model
        model.clientModel.service.set_cross_section(clientObject)

    @staticmethod
    def DeleteCrossSection(cross_sections_no: str = '1 2', model = Model):
        '''
        Args:
            cross_sections_no (str): CrossSections Number
            model (RSECTION Class, optional): Model to be edited

        '''

        # Delete from client model
        for section in ConvertStrToListOfInt(cross_sections_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_CROSS_SECTION.name, section)