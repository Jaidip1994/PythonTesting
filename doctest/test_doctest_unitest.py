import shape_area
import unittest
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(shape_area))
    return tests