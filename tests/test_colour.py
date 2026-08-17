import cv2

from src.colour.rgb_hsv import convert_to_rgb_hsv
from src.colour.histogram import calculate_rgb_histogram
from src.colour.statistics import calculate_rgb_statistics


IMAGE_PATH = "data/sample.jpg"


def test_rgb_hsv_conversion():
    original, rgb, hsv = convert_to_rgb_hsv(IMAGE_PATH)

    assert original is not None
    assert rgb is not None
    assert hsv is not None


def test_rgb_histogram():
    image = cv2.cvtColor(
        cv2.imread(IMAGE_PATH),
        cv2.COLOR_BGR2RGB
    )

    histograms = calculate_rgb_histogram(image)

    assert len(histograms) == 3


def test_colour_statistics():
    image = cv2.cvtColor(
        cv2.imread(IMAGE_PATH),
        cv2.COLOR_BGR2RGB
    )

    statistics = calculate_rgb_statistics(image)

    assert len(statistics) == 3
    assert "Red" in statistics
    assert "Green" in statistics
    assert "Blue" in statistics