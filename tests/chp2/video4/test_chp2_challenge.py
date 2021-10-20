from scripts.chp2.video4.mapmaker_challenge import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Senegal", 99.6937, -189.44406)
    assert str(exp.value) == "Invalid latitude, longitude combination."


def test_city_name():
    p1 = Point("Santiago", 13.1234, 20.5678)
    assert p1.get_name() == "Santiago"


def test_invalid_city_name():
    with pytest.raises(TypeError) as exp:
        Point(1313, 99.1234, -60.1313)
    assert str(exp.value) == "Invalid Name. City name has to be a String."
