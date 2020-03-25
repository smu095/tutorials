# Fluent Python
*Luciano Ramalho (2015)*

This folder contains a series of notebooks summarising the most relevant
chapters of [Fluent Python (Ramalho, 2015)](https://www.oreilly.com/library/view/fluent-python/9781491946237/).

These notes are not meant to be a substitute for the source material; they are
merely a summary of each chapter for future reference. Interested readers are
strongly encouraged to purchase a copy of the book, which goes into far more
detail.

## Part 1. Prologue

### [Chapter 1: The Python Data Model]()

This chapter describes the Python data model. The data model can be thought of as a description of Python as a framework. It formalises the interfaces of the building blocks of the language itself, such as sequences, iterators, functions, classes, context managers and so on.

## Part 2. Data Structures

### [Chapter 2: An Array of Sequences]()

This chapter discusses the variety of sequences in Python. Understanding them saves us from reinventing the wheel, and their common interface lets us create APIs that properly support and leverage existing and future sequence types.

### [Chapter 3: Dictionaries and Sets]()

This chapter discusses common dictionary methods, special handling for missing keys, variations of `dict` in the standard library, the `set` and `frozenset` types and how hash tables work

### Chapter 4: Text versus Bytes

This chapter delves deeper into Unicode. We have skipped this chapter for the time being.

## Part 3. Functions as Objects

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

## Part 4. Object-Oriented Idioms

### [Chapter 8: Object References, Mutability, and Recycling]()

This chapter discusses how names are bound to objects, the concepts of objects identity, value and aliasing, garbage collection, the `del` statement and weak referencing.
