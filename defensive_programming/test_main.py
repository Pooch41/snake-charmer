import pytest
from main import number_from_list_of_digits

def test_normal_case():
    assert number_from_list_of_digits([1, 4, 0]) == 140
    assert number_from_list_of_digits([2, 4]) == 24
    assert number_from_list_of_digits([1, 4, 0, 3 , 4]) == 14034


def test_zero_case():
    assert number_from_list_of_digits([0]) == 0
    assert number_from_list_of_digits([0, 0, 0, 0]) == 0000

def test_value_error_case():
    with pytest.raises(ValueError):
        number_from_list_of_digits([1, 2, -1])

    with pytest.raises(ValueError):
        number_from_list_of_digits([-1])

    with pytest.raises(ValueError):
        number_from_list_of_digits([1, -1, 0])

def test_type_error_case():
    with pytest.raises(TypeError):
        number_from_list_of_digits([1, 2, "a"])

    with pytest.raises(TypeError):
        number_from_list_of_digits(["a"])

    with pytest.raises(TypeError):
        number_from_list_of_digits(["a", "a", "a"])

def test_empty_case():
    with pytest.raises(ValueError):
        number_from_list_of_digits([])

    with pytest.raises(TypeError):
        number_from_list_of_digits()


pytest.main()