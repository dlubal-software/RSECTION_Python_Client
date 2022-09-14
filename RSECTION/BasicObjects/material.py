from RSECTION.initModel import Model, clearAtributes, ConvertStrToListOfInt
from RSECTION.enums import ObjectTypes

class Material():

    def __init__(self,
                 no: int = 1,
                 name: str = 'Grade S275',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:

        '''

        # Client model | Material
        clientObject = model.clientModel.factory.create('ns0:material')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Material No.
        clientObject.no = no

        # Material Name
        clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add material to client model
        model.clientModel.service.set_material(clientObject)

    @staticmethod
    def DeleteMaterial(materials_no: str = '1 2', model = Model):

        '''
        Args:

        '''

        # Delete from client model
        for material in ConvertStrToListOfInt(materials_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_MATERIAL.name, material)