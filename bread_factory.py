# Create a class

class NaanFactory:

    def make_dough(self, *ingredients):
        for items in ingredients:
            ingredient = items.lower()
            if ingredient == "water" and ingredient == "flour":
                return "dough"
            else:
                return "You need flour and water to make dough"


bread_factory = NaanFactory()
print(bread_factory.make_dough("water", "flour"))
