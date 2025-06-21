import pytest
from simple_math import SimpleMath

@pytest.mark.parametrize("number, expected", [
    (2, 4),
])
def test_square(number, expected):
    assert SimpleMath.square(number) == expected


@pytest.mark.parametrize("number, expected", [
    (-3, -27),
])
def test_cube(number, expected):
    assert SimpleMath.cube(number) == expected