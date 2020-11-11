# TDD Bread Factory! :bread:

## Timings

60-90 Minutes

## Summary

TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy!

What they do is before they make any new bread, they make a test to make sure the end output is correct. Then they adjust the recipe until it's just right!

You are going to do the same with bread! This is called Test Driven Development.

## Tasks

This exercise is going to bring together lots of concepts.

### Learning Outcomes
Learning outcomes include:
- git
- github
- functions
- TDD
- Separation of concerns - this is important do not ignore!
- DRY code
- DOD


## Installing and running
* install pytest using `pip install`
* To run the naan factory do the following:

```python
import naan factory
run factory()
```


### TDD - test driven development

1. write the test
```
# import all the relative packages
from bread_factory import NaanFactory
import unittest
import pytest

# create a class to test the  methods
class test_factory(unittest.TestCase):
    # create an object for the Naan Factory
    factory = NaanFactory()
    
    # create a method that tests each method within the factory object with the arguments passed through
    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough('water', 'flour'), 'dough')
        self.assertEqual(self.factory.make_dough('water', 'egg'), 'Both water and flour is needed')

    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_bread('Yes'), 'naan')
        self.assertEqual(self.factory.bake_bread('no'), 'make the dough')

    def test_run_factory(self):
        self.assertEqual(self.factory.run_factory(True), 'factory is ready to run')
        self.assertEqual(self.factory.run_factory(False), 'bake the naan')
```
2. run it with `python -m pytest`, and read the error
    * this would produce an error because we have not written the code in the file that we are testing

3. code and make it pass the test
```
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
```

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

##### Unit Tests

Test single pieces of code. Like a function.

**base of a test**
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with know variables
- asserting for expect output




### User stories for Naan Factory

```
#1
As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake dough with dough to get naan.

#3
As a user, I can user the run factory with water and flour and get naan.

```

## Acceptance Criteria

* you have written tests
* test pass
* you have written more test to make sure everything works as indented
* all user stories are satisfied
* code does not break
* code has exit condition
* DOD if followed