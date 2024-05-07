'''
A python Module is a file containing python definition and statement. The Python Standard Library contain a set of
predefined standard

When And Why Modules?
1. To maintain large project. By maintaining separate code for different logic.
2. Since we have different file for different logic it's easy to "de-bug".
3. Reduces code redundancy.

How To Create Module?
Syntax:
import module_name
import module_name as aliasing
from module_name import var_name, fun_name, ...., fun_n_name
from module_name import func_name as aliasing
import module_name *
'''

# Simple module
print('Module loaded')

def func1():
    print('func1 called')


def func2():
    print('funct2 called')