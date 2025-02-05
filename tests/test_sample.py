#import unittest
from ..parser import *

def add_two_number(x,y):
    return x+y

def test_add_two_number():
    assert add_two_number(1,2) == 3
