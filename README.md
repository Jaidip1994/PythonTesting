# Imp Things Learnt

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
