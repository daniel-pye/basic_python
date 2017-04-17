Basic Python
============

This repo contains scrips created while exploring the basics of the Python programming language and my solutions to Python challenges.

This readme file is also a curated notbook of tips and tricks picked up during the process.

# Data Types and Structures

## Numbers

* Division / always returns a float 0.0, whereas floor division // always returns an integer

* In interactive mode, the last printed expression is assigned to the variable

## Sequences

* Loop over two or more sequences at the same time using the `zip()` function:
```python
    for one, two in zip(var_list1, var_list2)
```

* Loop over a sequence in reverse using the `reversed()` function:
```python
    for i in reversed(range(1, 10, 2))
```

* Loop over a sequence in a sorted order using the `sorted()` function:
```python
    var = ['val1', 'val2', 'val3']
    for v in var sorted(set(var))
```

## Strings

* Strings should be enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes.

* To stop \n being interpreted as a newline, use raw strings. i.e. `print(r'C:\some\name')`

* Strings can be added together with + and repeated with *

* Strings have indices starting on the left at index 0. From right to left, string indices start a -1

* Strings can be sliced: `string[start:stop:step]`. If you omit the start point [:5] the first index defaults to 0. If you omit the stop point [0:] the last index defaults to the length of the string. Negative slices can be made string[-2:] and this can be used to reverse the `string[::-1]`

* The built-in function `len()` returns the length of a string

* Use the `str.format()` method to replace fields in strings denoted with curly {} braces.
```python
word = "string"
word2 = "thing"
"This is a {} {}.".format(word, word2)
```
* Replace letters or numbers in strings using the `replace(old, new)` method.

* Format a string containing a number, limiting the number to set decimal places using `'{0:.2f}'.format(arg)`.

## Lists

* Lists can be sliced like all built-in sequence types, `lst[0:10:2]`, returning a new "shallow" copy of the list

* Values in lists can be changed and/or replaced. Replace a value using the index: `lst[3] = 77`. Add to the end of a list using the append method: `list.append(168)`. Lists can also be modified in segments using slices: `lst[1:5] = [55, 66, 77, 88]`, removed `lst[1:5] = []`, or the entire list cleared of all values: `lst[:] = []`.

* Like strings, the `len()` function can also be applied to lists: `len(lst)`.

* Lists can also be nested in container lists: `lst = [['a', 'b', 'c'], [1, 2, 3]]`.

* You can append all of the items in an iterable using `extend(iterable)`

* An item can be inserted into a list at a given position using `insert(i, x)`

* Remove an item from a list using `remove(i, x)`

* Pop an item out of a list using `pop([i])`. If no item is specified, it will pop the last item in the list.

* Remove all items in a list with `clear()`

* Count the instances of a value in a list using `count(x)`

* Sort items in a list using `sort(key=None, reverse=False)`

* Reverse elements in a list using `reverse()`

* Copy a list using `copy()`

* Lists can be used as stacks using the `append()` and `pop()` methods

* To filter data in a list, create a new list and run an if statement condition in a for loop to act as the filter, appending values found in the original list to the new one.

* To use lists as a queue -- i.e. "first in, first out" -- import [deque](https://docs.python.org/3/library/collections.html#collections.deque) from the collections module. Deque uses `append(x)`, `appendleft(x)`, `clear()`, `copy()`, `count(x)`, `extend(iterable)`, `extendleft(iterable)`, `insert(i, x)`, `pop()`, `popleft()`, `remove(value)`, `reverse()`, `rotate(n)`, and `maxlen` methods.

* Remove an item from a list given its index rather than value using the `del` statement.
```python
    a = [1, 2, 3, 4, 5]
    del a[0]
```

### List comprehensions

* Listcomps consist of square brackets containing an expression followed by a for clause.
```python
    squares = [x**2 for x in range(10)]  # Creates a list of squares
```

* Filtering can be added to list comprehensions using the if statement.
```python
    even_squares = [x * x for x in range(10) if x % 2 == 0]

    values = [ expression for value in collection if condition ]
```

## Tuples

* Tuples always output data nested in parenthesis, but can be input without parenthesis. Tuples are immutable, but you can reassign items in a tuple if it contains mutable items such as lists. A tuple with just one value is created by adding a comma after the value: `single_value_tuple = ('value',)`

* Tuples, like other sequences, can be packed and unpacked.
```python
    tuple = 1, 2, 3
    a, b, c = tuple
```

## Sets

* Sets are an unordered collection with no duplicate elements. They support mathematical operations such as union, difference, and symmetric difference. Sets are created by assigning curly braces {} or with the `set()` function. Set comprehensions are supported.

## Dictionaries

* Dictionaries, unlike lists and tuples, are of the mapping type. Key-value pairs can be deleted using the del keyword.

* Output a list of a dictionary's keys using `list(d.keys())` for an arbitrary list or `sorted(d.keys())` for a sorted list.

* Check to see if a single key is in a dictionary using the `in` keyword.

* Use the `dict()` constructor to build dictionaries from key-value pair sequences. Dict comprehensions can be used to create expressions:
```python
    {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}
```

  They can also be specified using kwargs if they are simple strings:
```python
    dict(something=4139, another=4127, one_more=4098)
```

* Key-value pairs can be retreived using the `items()` method.

# Control Flow

## Conditionals and loops

* Use the `if`, `elif`, `else` statement to test whether specific conditions are true.

* Use the `while` statement to repeatedly test whether its expression is true.

* Use the `for` statement to iterate over the elements in a sequence, such as a string, tuple or list. Use a break statement in a for loop to end the iteration early, or a continue statement to skip the rest of a block and continue with the next item. The `range()` function returns an iterator of integers that can be used in a for loop: `list(range(x, x))`.

* It's recommended to first make a copy of a list to iterate over if you need to modify it as the iteration does not itself make a copy. This can be achieved using slice notation:
```python
    for word in words[:]:
        if len(word) > 5:
            words.insert(0, word)
```

* To iterate over the indices of a sequence, you can combine the `len()` and `range()` functions:
```python
    variable = ['some', 'text', 'in', 'a', 'list']
    for word in range(len(variable))
        print(word, variable[word])
```

*  However, the `enumerate()` function may be more convenient. Enumerate returns a tuple in the format (count, value). The `list()` function creates lists from iterables. The count starting poiint can be modified:
```python
    first_quarter = ['January', 'February', 'March']
    list(enumerate(first_quarter, start=1))
```

* For statements can have an else clause which executes when the loop terminates wither through exhaustion of iteration over a list or when a while loop statement becomes False.

* A pass statement can be used either when creating minimal classes, when it is required syntactically but needs no action, or as a placeholder while working on new code.

## Functions

* Functions are defined using the def keyword, which is followed by the function name and a parenthesised list of parameters and a colon. On the next line, indented, a docstring can be added, followed by the function statement(s).
```python
    def function_name(param1, param2, *args, **kwargs):
        """ Docstring """
        Function statements
```

* Variables assigned in functions operate in a local scope within the function and are not callable outside of it, unless a global statement is used:
```python
    def function(param):
        global var
        var = "something"
```

* The `return` statement returns a value from a function. It will return None without an expression.

* The `in` keyword tests whether a sequence contains a certain value.

* Functions can be defined using arguments in three forms: default argument values e.g. `def function(prompt, retries=5, reminder='Please try again.')`; keyword arguments e.g. `def function(positional arg, optional_arg='something')` where the order of kwargs passed to the function is not important; and arbitrary argument lists where the args are wrapped in a tuple e.g. `def multiple_items(file, separator, *args)`.

* A formal parameter passed to a function of the type `**kwargs` receives a dictionary that will contain all additional kwargs not corresponding to another formal parameter.

### Unpacking lists/tuples and dictionaries with *args and **kwargs

* If you have args already in a list or tuple that need to be unpacked for a function, use `*args` to unpack.
```python
    args = [3, 9]
    list(range(*args))

    returns [3, 4, 5, 6, 7, 8]
```

* To unpack dictionaries for use in functions, use `function(**var)` to call the function using the variable for the dictionary.

# Modules

* If a module's function will be used often in a script, it can be assigned to a local variable:
```python
    exit = sys.exit
```

# I/O

* To convert a value or values to a string, use the `str()` or `repr()` functions.

