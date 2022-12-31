from stack.laskin import Laskin
import pytest

@pytest.fixture
def laskin():
    return Laskin()

def test_constructor():
    s = Laskin()
    assert isinstance(s,Laskin)

def test_kertolasku(laskin):
    assert laskin.kertolasku(2,5) == 10

def test_yhteenlasku(laskin):
    assert laskin.yhteenlasku(5,6) == 11

def test_vahennyslasku(laskin):
    assert laskin.vahennyslasku(5,3) == 2

def test_jakolasku(laskin):
    assert laskin.jakolasku(10,5) == 2.0
    assert laskin.jakolasku(10,0) == ZeroDivisionError
    