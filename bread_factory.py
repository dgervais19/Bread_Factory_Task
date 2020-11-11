# import json to convert the arguments into a list
import json
class NaanFactory:

    def make_dough(self, *ingredients):
        ingredients_list = json.dumps(ingredients)
        if "water" in ingredients_list and "flour" in ingredients_list:
            return 'dough'
        else:
            return 'Both water and flour is needed'

    def bake_bread(self, made_dough):
        if made_dough == 'yes' or made_dough == 'Yes':
            print("Great! now you can put it in the oven")
            return 'naan'
        else:
            return 'make the dough'

    def run_factory(self, baked_naan):
        if baked_naan:
            return 'factory is ready to run'
        else:
            return 'bake the naan'





if __name__ == '__main__':
    bread_factory = NaanFactory()
    print(bread_factory.make_dough('water', 'flour'))

    print(bread_factory.bake_bread())