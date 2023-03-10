from start import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (8, 4, 2),
                                                   (30, -3, -10)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)