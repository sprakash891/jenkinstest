import pytest

print ("This is Jenkins traning, I am from test_school.py")

@pytest.mark.arithemetic
def test_mul():
   print ("This is multiply function")

@pytest.mark.arithemetic
def test_sub():
   print ("This is subtraction function")

@pytest.mark.logical
def test_not():
   print ("This is NOT function")

