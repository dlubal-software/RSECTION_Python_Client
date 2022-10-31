from RSECTION.initModel import Model, clearAtributes

class LoadCombination():

    def __init__(self,
                 no: int = 1,
                 load_combination_item: list = None,
                 user_defined_name: list = [False],
                 to_solve: bool = True,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:

        '''

        #Cleint model | Load Combination
        clientObject = model.clientModel.factory.create('ns0:load_combination')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Load Combination No.
        clientObject.no = no

        # User Defined Name
        if user_defined_name[0]:
            clientObject.user_defined_name_enabled = user_defined_name[0]
            clientObject.name = user_defined_name[1]

        # Load Combination to_solve enable/disable option
        clientObject.to_solve = to_solve

        # Load Combination Items List
        clientObject.items = model.clientModel.factory.create('ns0:load_combination.items')

        for i,j in enumerate(load_combination_item):

            lcir = model.clientModel.factory.create('ns0:load_combination_items_row')
            lcir.no = i+1
            lcir.row.factor = load_combination_item[i][0]
            lcir.row.load_case = load_combination_item[i][1]
            lcir.row.amplitude_function_type = "CONSTANT"

            clientObject.items.load_combination_items.append(lcir)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Load Combination to client model
        model.clientModel.service.set_load_combination(clientObject)

