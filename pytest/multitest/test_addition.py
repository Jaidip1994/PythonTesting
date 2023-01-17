import cal

def test_add_int():
    result = cal.add(2,5)
    assert result == 7

def test_add_float():
    result  = cal.add(2.5, 2.5)
    assert result == 5.0

def test_add_str():
    result= cal.add('Jai', 'dip')
    assert result == 'Jaidip'