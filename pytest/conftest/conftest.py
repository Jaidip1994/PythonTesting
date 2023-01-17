import pytest
import os


@pytest.fixture
def write_file():
    print("\n Creating File")
    f = open("append_file.txt", "w+")

    for i in range(10):
        f.write("\n X Y Z %d" % (i + 1))

    f.flush()
    yield f

    print("\n Closing File")
    f.close()


@pytest.fixture
def readonly_file():
    print("\n Creating File")
    f = open("readonly_file.txt", "w+")

    for i in range(10):
        f.write("\n X Y Z %d" % (i + 1))

    f.close()
    f = open("readonly_file.txt", "r")
    yield f

    print("\n Closing File")
    f.close()
