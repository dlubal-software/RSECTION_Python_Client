from RSECTION.initModel import Model, clearAtributes
from RSECTION.enums import *

class LoadCase():

    def __init__(self,
                 no: int = 1,
                 action_category = ActionCategoryType.ACTION_CATEGORY_PERMANENT_G,
                 to_solve: bool = True,
                 name: str = '',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Load Case Tag
            action_category (enum): Action Category Type Enumeration
            to_solve (bool): Enable/Disable To Solve Option
            name (str): User Define Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        #Cleint model | Load Case
        clientObject = model.clientModel.factory.create('ns0:load_case')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Load Case No.
        clientObject.no = no

        # Load Case Name
        clientObject.name = name

        # Load Case to_solve enable/disable option
        clientObject.to_solve = to_solve

        # Load Case Action Category Assign
        clientObject.action_category = action_category.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Load Case to client model
        model.clientModel.service.set_load_case(clientObject)



