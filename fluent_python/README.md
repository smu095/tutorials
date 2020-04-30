# Fluent Python
*Luciano Ramalho (2015)*

This folder contains a series of notebooks summarising the most relevant
chapters of [Fluent Python (Ramalho, 2015)](https://www.oreilly.com/library/view/fluent-python/9781491946237/).

These notes are not meant to be a substitute for the source material; they are
merely a summary of each chapter for future reference. Interested readers are
strongly encouraged to purchase a copy of the book, which goes into far more
detail.

This repository has the following structure:

```
.
├── README.md
├── examples            <- modules containing example code
├── figs                <- figures used in notebooks
├── notebooks           <- notebooks containing summary notes of each chapter
├── requirements.txt    <- project requirements
└── setup.py            <- makes repo pip installable
```

The notebooks follow the naming convention `part.chapter-chapter-name.ipynb`.

## Part I: Prologue

### [Chapter 1: The Python Data Model]()

This chapter describes the Python data model. The data model can be thought of as a description of Python as a framework. It formalises the interfaces of the building blocks of the language itself, such as sequences, iterators, functions, classes, context managers and so on.

## Part II: Data Structures

### [Chapter 2: An Array of Sequences]()

This chapter discusses the variety of sequences in Python. Understanding them saves us from reinventing the wheel, and their common interface lets us create APIs that properly support and leverage existing and future sequence types.

### [Chapter 3: Dictionaries and Sets]()

This chapter discusses common dictionary methods, special handling for missing keys, variations of `dict` in the standard library, the `set` and `frozenset` types and how hash tables work

### Chapter 4: Text versus Bytes

This chapter delves deeper into Unicode. We have skipped this chapter for the time being.

## Part III: Functions as Objects

### [Chapter 5: First-Class Functions]()

This chapter discusses functions as first-class objects, meaning they can be

* created at runtime,
* assigned to a variable or element in a data structure,
* passed as an argument to a function,
* returned as the result of a function.

Having first-class functions enables programming in a functional style.

### [Chapter 6: Design Patterns with First-Class Functions]()

This chapter discusses design patterns in the context of languages with first-class functions. The general idea is that one can replace instances of some participant in these patterns with simple functions, thus reducing boilerplate code.

### [Chapter 7: Function Decorators and Closures]()

The goal of this chapter is to explain how function decorators work. It explores the Python decorator syntax, how Python decides whether a variable is local, why closures exist and how they work. This is helpful when we want to mplement a well-behaved decorator. This chapter also covers interesting decorators in the standard library and implementing a parameterised decorator.

## Part IV: Object-Oriented Idioms

### [Chapter 8: Object References, Mutability, and Recycling]()

This chapter discusses how names are bound to objects, the concepts of objects identity, value and aliasing, garbage collection, the `del` statement and weak referencing.

### [Chapter 9: Pythonic Objects]()

This chapter picks up where chapter 1 left off, and shows how to implement several special methods that are commonly seen in Python objects of many different types.

We will see how to:

* Support the built-in functions that produce alternative object representation.
* Implement an alternative constructor as a class method.
* Extend the format mini-language used by the `format()` built-in and `str.format()` method.
* Provide read-only access to attributes.
* Make an object hashable for use in sets and `dict` keys.
* Save memory by using `__slots__`.
Through examples we will also examine:
* How and when to use the `@classmethod` and `@staticmethod` decorators.
* Private and protected attributes in Python: usage, conventions, and methods.


### [Chapter 10: Sequence Hacking, Hashing, and Slicing]()

This chapter introduces protocols and duck typing. The working example is a generalised implemetation of the `Vector2d` class from the previous chapter, extending it to the multidimensional case, allowing it to support:

* Basic sequence protocol: `__len__`, `__getitem__`.
* Safe representation of many instances with many items.
* Proper slicing support, producing new `Vector` instances.
* Aggregate hashing taking into account every contained element value.
* Custom formatting language extension.
* Dynamic attribute access with `__getattr__`.

### [Chapter 11: Interfaces: From Protocols to ABCs]()

The subject of this chapter is interfaces, from the dynamic protocols that characterise duck typing to abstract base classes (ABCs) that make interfaces explicit and verify implementations for conformance.

### [Chapter 12: Inheritance: For Good or For Worse]()

This chapter is about inheritance and subclassing, discussing good and bad practices when building class hierarchies. Multiple inheritance is illustrated using two important Python projects: the TKinter GUI toolkit and the Django Web framework.

### [Chapter 13: Operator Overloading: Doing It Right]()

This chapter deals mainly with infix and unary operators. It covers:

* How Python supports infix operators with operands of different types.
* Using duck typing or explicit type checks to deal with operands of various types.
* How an infix operator method should signal it cannot handle an operand.
* The special behaviour of the rich comparison operators (e.g., `==`, `>`, `<`, `<=`, etc.).
* The default handling of augmented assignment operators, like `+=`, and how to overload them.


## Part V: Control Flow

### [Chapter 14: Iterables, Iterators, and Generators]()

This chapter is about the [Iterator pattern](https://en.wikipedia.org/wiki/Iterator_pattern), which among other things lets us *lazily* fetch items one at a time when scanning datasets that don't fit in memory. The Iterator pattern is built into Python. This chapter covers the following topics (and more):

* How the `iter(...)` built-in function works
* How to implement the Iterator pattern
* How a generator function works in detail
* How the Iterator pattern can be replaced by a generator function or expression
* General purpose generator functions from the standard library
* Using the new `yield` statement to combine generators