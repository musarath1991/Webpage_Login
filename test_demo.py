##1

import pytest

@pytest.mark.login
def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is mot equal to b"

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.login
def test_m3():
    assert True

def test_m4():
    assert False

@pytest.mark.login
def test_m5():
    assert 100 == 100

@pytest.mark.skip
def test_m6():
    assert "musarath" == "MUSARATH"

@pytest.mark.login  #if we give "py.test test_demo.py -m login", only marked test cases will execute. "m" for marker
def test_login_FB():
    assert "admin" == "admin123"

#execute in commant line  right click on pgm and open in terminal -->  pytest test_demo.py
# result will be  .F.F.F ==> . will be green and F will be red

#execute particular test case  ==> "py.test test_demo.py -k test_m6 -v"
#we can give just m6. no need to give full test name.


