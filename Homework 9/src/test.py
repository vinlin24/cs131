"""test.py

For scratch work.
"""

def e(b: bool) -> bool:
    print("e")
    return b

def f(b: bool) -> bool:
    print("f")
    return b

def g(b: bool) -> bool:
    print("g")
    return b

def h(b: bool) -> bool:
    print("h")
    return b

def do_something():
    print("do_something")

if e(False) or f(True) and g(True) or h(True):
    do_something()
