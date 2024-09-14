import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixture.. \n")
    city = ['New York', 'London', 'Rio', 'Paris', 'Lisboa']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == "New York"
    assert setup_list[::2] == ['New York',  'Rio', 'Lisboa']

def myReverse(lst):
    lst.reverse()
    return lst

def test_reverseList(setup_list):
    assert setup_list[::-2] == ['Lisboa',  'Rio', 'New York']
    assert setup_list[::-1] == myReverse(setup_list)