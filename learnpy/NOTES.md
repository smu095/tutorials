# General programming skills

## Understanding Python's execution model
[This post by Jeff Knupp](https://jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/) describes how Python's execution model works. We summarise the post briefly in the following:

* Everything in Python is an **object**.
* Values, classes, functions, object instances, etc., all have the properties usually associated with objects in the object oriented sense; types have member functions, functions have attributes, modules can be passed as arguments, etc.
* Instead of variables, Python has **names** and **bindings**.
* In the following example `foo` is a *name that has a binding to the object created by* `Foo()`. 

```python
# Names and bindings
class Foo(): 
    pass

foo = Foo()
baz = foo
```

* `baz` is a new name with a binding to the same object that `foo` is bound to. Changing `foo` will be reflected in `baz`. 
* Binding a name to an object doesn't change it. Changing some property of the object, however, will be reflected in all other names bound to that object.
* There are two types of objects in Python: **mutable** and **immutable**.
* Values of mutable objects (e.g. a `list`) can be changed after they are created, immutable objects (e.g. a `tuple`) cannot.
    * **Note:** The "value" of e.g. a `tuple` is conceptually the same as a sequence of names associated with *unchangeable* bindings to objects.
    * **Key:** The bindings are unchangeable, but the *underlying objects are not*. 
* What happens when we pass variables (that are just names bound to objects) to **functions**? See the following example:
 
 ```python
 def list_changer(input_list):
    input_list[0] = 10

    input_list = range(1, 10)
    print(input_list)
    input_list[0] = 10
    print(input_list)

>>> test_list = [5, 5, 5]
>>> list_changer(test_list)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[10, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print test_list
[10, 5, 5]
```

* This is an example of Python's **scoping** rules.
* When a name is bound to an object, that name is only usable within the name's **scope**.
* The scope of a name is determined by the **block** (i.e. "block" of Python code executed as a single unit) in which it was created.
    * The three most common types of blocks are **modules**, **class definitions** and **function bodies**.
* The interpreter finds the binding of a name by
    1. Checking the innermost block.
    2. Checking the scope that contained the innermost block.
    3. Checking the scope that contained ii., and so on.
* The outermost scope contains **global** names. These can be accessed from anywhere.
* There are two keywords that allows the interpreter to **use preexisting bindings**:
    1. `global var` tells the interpreter to use the binding of `var` in the **outermost ("global") scope**. Will create `var` if it does not already exist.
    2. `nonlocal var` tells the interpreter to use the binding defined in the **nearest enclosing scope**. Note that `var` must already exist in order to be referenced by `nonlocal`.

## Python Classes and Object Oriented Programming
[This post by Jeff Knupp](https://jeffknupp.com/blog/2017/03/27/improve-your-python-python-classes-and-object-oriented-programming/) gives a brief overview over object oriented programming in Python.

* A `class` is a logical grouping of data and functions (referred to as methods). By logical grouping we mean that there is a logical connection between the components (i.e. data and methods) of the class.
* Classes can be thought of as **blueprints** for creating objects.

```python
class WebProgrammer:
    
    def __init__(self, name, age):
        self.name = name
	self.age = age
        self.wages = wages
```

* The `__init__` method (with proper number of arguments) creates the object, which is known as an **instance** of the class.
* **Attributes** in `__init__` ("normal" attributes) are typically preceded by the `self` parameter, which *refers to this particular instance of the class*.
    * Conceptually, these are the same:
        * sean = Programmer("Sean", 35)
        * sean = Programmer(sean, "Sean", 35)
* **Rule of thumb:** Don't introduce new attributes outside of `__init__` (object consistency).
* A function defined in a class is called a **method**. Methods require an instance of the object, and are therefore often referred to as **instance methods**. They have access to all the data contained in the instance of an object, and are passed the `self` parameter as the first argument.

```python
class WebProgrammer:
    
    def __init__(self, name, age):
        self.name = name
	self.age = age
        self.wages = wages

    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old and I am a programmer!")
```

* **Class attributes** are set at a class level and don't require `self`. This means they can be referenced without instantiating an object. E.g.:

```python
class WebProgrammer:

    species = 'Human'
    
    def __init__(self, name, age):
        self.name = name
	self.age = age
        self.wages = wages

    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old and I am a programmer!")
    
    def pay_raise(self):
        return self.wages * 1.05

print(Worker.species)
# 'Human'
```

* Similarily, **static methods** don't have access to `self` and do not require an instance of a class.
* The `@staticmethod` decorator is used to make it clear that this method should not receive the instance as the first parameter.
* We generally use static methods to create **utility functions** ([source](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)).


```python
class WebProgrammer:

    species = 'Human'
    
    def __init__(self, name, age):
        self.name = name
	self.age = age
        self.wages = wages

    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old and I am a programmer!")
    
    def pay_raise(self):
        return self.wages * 1.05
    
    @staticmethod
    def sigh():
        print('Sigh!') 

print(Worker.sigh())
# 'Sigh!'
```

* A variant of the static method is the **class method**. Instead of receiving the instance as the first parameter, it is passed the class parameter `cls`. 
* Class methods are generally used to to create factory methods. Factory methods return class object (similar to a constructor) for different use cases ([source](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)).
* Class methods are mainly used in conjunction with **inheritance**. Inheritance is the process by which a "child" class inherits the data and behaviour of a "parent" class.
* Inheritance is useful when there is a lot of repetition in a class. Consider the following example of a data scientis, which is specialised kind of programmer:


```python
class DataScientist:

    species = 'Human'
    
    def __init__(self, name, age):
        self.name = name
	self.age = age
        self.wages = wages

    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old and I am a programmer!")
    
    def pay_raise(self):
        return self.wages * 1.20
    
    @staticmethod
    def sigh():
        print('Sigh!') 
```

* `DataScientist` is almost identical to `Programmer`. We can abstract away the similiarities of being a data scientist and a webprogrammer into a class called `Programmer`.
* To do this we create an **abstract base class** `Programmer` which `WebProgrammer` and `DataScientist` inherit from.

```python
from abc import ABC, abstractmethod

class Programmer(ABC):

    species = 'Human'
    
    def __init__(self, name, age):
        self.name = name
	self.age = age
        self.wages = wages

    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old and I am a programmer!")
    
    @abstractmethod
    def pay_raise(self):
        pass
    
    @staticmethod
    def sigh():
        print('Sigh!') 


class WebProgrammer(Programmer):

    def pay_raise(self):
        return self.wages * 1.05

class DataScientist(Programmer):

    def pay_raise(self):
        return self.wages * 1.20
```

* Inheritance is the key to the **Liskov substitution principle** (LSP), one of the five [SOLID](https://en.wikipedia.org/wiki/SOLID) sofware design principles.
* LSP states that we *should be able to use a child class wherever a parent class is expected with no problems*.

## Writing Better Python Functions
[This post by Jeff Knupp](https://jeffknupp.com/blog/2018/10/11/write-better-python-functions/) gives an overview over what makes functions "bad" or "good".

* A **good function** in Python can tick off the following boxes:
    - [ ]  Is sensibly named.
    - [ ]  Has a single responsibility ([SOLID](https://en.wikipedia.org/wiki/SOLID)).
    - [ ]  Includes a docstring.
    - [ ]  Returns a value.
    - [ ]  Is not longer than 50 lines.
    - [ ]  Is *idempotent* and, if possible, *pure*.

* **Naming:** It should be clear from the function name what the function does. Avoid unnecessary abbreviations that are not common knowledge. Bonus if the arguments help to clarify intent.

```{python}
# Bad
get_knn_from_df(df)

# Good
k_nearest_neighbours(dataframe)
```
* **Single responsibility:** A function should do *one thing and one thing only*. Main reasons for this are cleaner testing and easier maintenance. If your function name has the word `and` in it, odds are it does not have a single responsibility. 
* **Docstrings:** [PEP-257](https://www.python.org/dev/peps/pep-0257/) details Python's docstring conventions. Main takeaways:
    * *Every* function requires a docstring.
    * Use proper grammar and punctuation, write in complete sentences.
    * Begin with one-sentence summary of what the function does.
    * Use prescriptive rather than descriptive language (i.e. prescribe the function or method's effect as a command, e.g. "Do this", "Return that", *not* as a description; e.g. don't write "Returns the pathname ...").
* **Return values:** Every function should return a useful value, if only for testability purposes.
    * What if the function e.g. modifies something inplace? Return `True` if the modification is successful!
* **Function length:** The length of a function directly affects readability and thus maintainability. If a function is too long, it should be **refactored**.

* **Idempotency and functional purity:** 
    * An **idempotent** function will *always return the same value given the same set of parameters*, regardless of how many times it is called. Idempotency is important because it makes functions easy and fast to test. It also makes refactoring easy.
    * A **pure** function is idempotent and has *no observable side-effects*. 

> Pure functions do not have logging statements or print() calls. They do not make use of database or internet connections. They don't access or modify non-local variables. And they don't call any other non-pure functions. Makes testing and maintainability fast and simple.

* Note that idempotency and functional purity are aspirational, not required. In some cases, it is impossible to write idempotent and pure functions.
