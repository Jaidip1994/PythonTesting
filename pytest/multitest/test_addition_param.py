import cal
import pytest

@pytest.mark.parametrize('ip1, ip2, res', [(1,2,3), (2.5,2.5,5.0)])
def test_add(ip1, ip2, res):
    assert cal.add(ip1, ip2) == res