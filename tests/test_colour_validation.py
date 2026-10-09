import numpy as np
import pytest

from src.colour.histogram import calculate_rgb_histogram
from src.colour.statistics import calculate_rgb_statistics


@pytest.mark.parametrize(
    "invalid_image",
    [
        None,
        np.empty((0, 2, 3), dtype=np.uint8),
        np.zeros((4, 4), dtype=np.uint8),
        np.zeros((4, 4, 4), dtype=np.uint8),
        "not an image array",
    ],
    ids=["none", "empty", "grayscale", "four-channel", "wrong-type"],
)
@pytest.mark.parametrize(
    "feature_function",
    [calculate_rgb_histogram, calculate_rgb_statistics],
    ids=["histogram", "statistics"],
)
def test_rgb_feature_functions_reject_invalid_inputs(feature_function, invalid_image):
    with pytest.raises(ValueError, match="RGB image"):
        feature_function(invalid_image)


def test_rgb_histogram_counts_pixels_per_channel():
    image = np.array(
        [
            [[255, 0, 0], [255, 255, 0]],
            [[0, 255, 0], [0, 0, 255]],
        ],
        dtype=np.uint8,
    )

    red, green, blue = calculate_rgb_histogram(image)

    assert red.shape == (256, 1)
    assert green.shape == (256, 1)
    assert blue.shape == (256, 1)
    assert (red[0, 0], red[255, 0]) == (2, 2)
    assert (green[0, 0], green[255, 0]) == (2, 2)
    assert (blue[0, 0], blue[255, 0]) == (3, 1)


def test_rgb_statistics_return_expected_values():
    image = np.array(
        [
            [[255, 0, 0], [255, 255, 0]],
            [[0, 255, 0], [0, 0, 255]],
        ],
        dtype=np.uint8,
    )

    statistics = calculate_rgb_statistics(image)

    assert statistics["Red"] == {"mean": 127.5, "minimum": 0, "maximum": 255}
    assert statistics["Green"] == {"mean": 127.5, "minimum": 0, "maximum": 255}
    assert statistics["Blue"] == {"mean": 63.75, "minimum": 0, "maximum": 255}
