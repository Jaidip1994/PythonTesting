import pytest


def test_type():
    assert type(1 + 2) is int


def test_add_int():
    assert 2 + 5 == 9

@pytest.mark.skip(reason="Temporary Skipped")
def test_string():
    assert "u" in "sun"


def test_add_string():
    assert ("sunny" + "day") == "sunnyday"
