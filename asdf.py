>>> from constraint import *
>>> problem = Problem()
>>> problem.addVariable("a", [1,2,3])
>>> problem.addVariable("b", [4,5,6])
>>> problem.getSolutions()
[{'a': 3, 'b': 6}, {'a': 3, 'b': 5}, {'a': 3, 'b': 4},
 {'a': 2, 'b': 6}, {'a': 2, 'b': 5}, {'a': 2, 'b': 4},
 {'a': 1, 'b': 6}, {'a': 1, 'b': 5}, {'a': 1, 'b': 4}]
