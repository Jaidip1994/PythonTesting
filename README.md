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

----

## Pytest Framework

To Run a File using `pytest` use

```python
pytest <file name> -v
# Or
py.test <file name> -v
```

To run all the test file inside the current directory

```python
pytest -v
```

To execute only a single module

```python
pytest <module name>::<test name> -v
```

If we want to execute a test which is matching a substring

```python
pytest <module name> -v -k "<substr>"
```

If we want to execute a test with a substring and expression

```python
pytest <module name> -v -k "<substr1> or <substr2>"
pytest <module name> -v -k "<substr1> and <substr2>"
```