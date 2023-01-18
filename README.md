# Imp Things Learnt

## Unit Test Framework

- To run a Unit test based test class

```python
python -m unittest <testfile name> -v
```

- To Run a single test

```python
python -m unittest shape_test.TestArea.test_triangle -v
```

- To Run Multiple test selectively

```python
python -m unittest shape_test.TestArea.test_triangle shape_test.TestArea.test_rectangle -v
```

---

## Pytest Framework

- To Run a File using `pytest` use

```python
pytest <file name> -v
# Or
py.test <file name> -v
```

- To run all the test file inside the current directory

```python
pytest -v
```

- To execute only a single module

```python
pytest <module name>::<test name> -v
```

- If we want to execute a test which is matching a substring

```python
pytest <module name> -v -k "<substr>"
```

- If we want to execute a test with a substring and expression

```python
pytest <module name> -v -k "<substr1> or <substr2>"
pytest <module name> -v -k "<substr1> and <substr2>"
```

- If we want to stop execution of tests if one of the test failed then we need to use this flag `-x`

```python
pytest -v -x
```

- But if we want to keep a threshold if it crosses that then only stop the execution of all test, then with `-x` flag we need to also specify `--maxfail=<no>` Here `no` specifies an integer value which is a threshold i.e. tolerance value for number of failed test
  If we dont specify `maxfail` flag by default value is considered as `1`.

```python
pytest -v -x --maxfail=2
```

- If we want to control the traceback print option then we can use this flag.

```python
pytest --tb=style
# style can be (auto/long/short/line/native/no)
```

- If we want to execute test based on some `custom markers` then we can define the markers using the decorator `@pytest.mark.<markername>` and we can run test associated with the marker.

```python
pytest -v -m <marker name>
```

- If some test needs to be skipped use this decorator `@pytest.mark.skip(reason='')` Now to get the result summary of skip test use this command

```python
pytest -v -rsf
# r is for result summary
# s is to show skip test summary info
# f is to show failed test summary info
```

- Run test in quiet mode use this flag `-q`
- Enable Python debugging only for the failed test use this flag `--pdb`
- Enable Python debugging for each test case `--trace`
- To call the same function will multiple paramater use this decorator e.g. `@pytest.mark.parametrize('ip1, ip2, res', [(1,2,3), (2.5,2.5,5.0)])` here `ip1, ip2` are inputs and `res` is the result and as a list the different param values are provided.

---

## Doc test

Define test using Docstring, and then execute the test using.

```python
python -m doctest <filename> -v
```

If we want to run pytest but using doctest format

```python
python -m pytest --doctest-modules <filename> -v
```

If we want to run unittest framework using docttest, run the below command, but prior to that suite needs to be created. ex.

```python
python -m unittest <file_name> -v
```

File example to create suite

```python
import shape_area
import unittest
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(shape_area))
    return tests
```

- If we want to match only one part of the ouput then we can use elipses `...`
  and then we have use one directive called, `#doctest: +ELLIPSIS` and this will match except the `...` character
  ex.

```python
  class MyOwnObject:
    def __init__(self, name, number):
        self.name = name
        self.number = number


    def create_new_MyOwnObject(name, number):
    """
    >>> create_new_MyOwnObject('Jaidip',1) #doctest: +ELLIPSIS
    <doctest_object.MyOwnObject object at 0x...>
    """
    return MyOwnObject(name, number)
```

- To handle whitespace `#doctest: +NORMALIZE_WHITESPACE` this directive can be used.
