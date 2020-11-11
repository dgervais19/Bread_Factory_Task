# import json to convert the arguments into a set of data
import json

# create a class for the naan factory
class NaanFactory:

# create your functions
    def make_dough(self, *ingredients):
        # convert the arguments to a set of data and assign to a variable
        ingredients_list = json.dumps(ingredients)
        # check if water and flour are in that set
        if "water" in ingredients_list and "flour" in ingredients_list:
            return 'dough'
        else:
            return 'Both water and flour is needed'

    def bake_bread(self, made_dough):
        # if the dough has been made you can go to the next step and bake it
        if made_dough == 'yes' or made_dough == 'Yes':
            print("Great! now you can put it in the oven")
            return 'naan'
        else:
            return 'make the dough'

    def run_factory(self, baked_naan):
        # return 'factory is ready to run' if baked_naan is True
        if baked_naan:
            return 'factory is ready to run'
        else:
            return 'bake the naan'





if __name__ == '__main__':
    bread_factory = NaanFactory()
    print(bread_factory.make_dough('water', 'flour'))

    print(bread_factory.bake_bread())