Basic Python
============

This repo contains scrips created while exploring the basics of the Python programming language and my solutions to Python challenges.

This readme file is also a curated notbook of tips and tricks picked up during the process.

Notes
=====

# Data Types and Structures

## Numbers

* Division / always returns a float 0.0, whereas floor division // always returns an integer

* In interactive mode, the last printed expression is assigned to the variable

## Sequences



## Strings

* Strings should be enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes.

* To stop \n being interpreted as a newline, use raw strings. i.e. print(r'C:\some\name')

* Strings can be added together with + and repeated with *

* Strings have indices starting on the left at index 0. From right to left, string indices start a -1

* Strings can be sliced: string[start:stop:step]. If you omit the start point [:5] the first index defaults to 0. If you omit the stop point [0:] the last index defaults to the length of the string. Negative slices can be made string[-2:] and this can be used to reverse the string[::-1]

* This chart is helpful for visualising how indices point between characters in a string:
⋅⋅⋅ +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1

* The built-in function len() returns the length of a string

* Use the str.format() method to replace fields in strings denoted with curly {} braces.
```python
word = "string"
word2 = "thing"
"This is a {} {}.".format(word, word2)
```


## Lists



### List comprehensions



## Tuples



## Sets



## Dictionaries



# Control Flow

## Conditionals and loops


## Functions



# Modules


# I/O



