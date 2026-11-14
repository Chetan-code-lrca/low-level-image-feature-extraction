import numpy as np
import pytest

from src.colour.histogram import calculate_rgb_histogram


def test_normalized_histograms_sum_to_one_per_channel():
    image = np.array(
        [
            [[255, 0, 0], [255, 255, 0]],
            [[0, 255, 0], [0, 0, 255]],
        ],
        dtype=np.uint8,
    )

    histograms = calculate_rgb_histogram(image, normalize=True)

    assert len(histograms) == 3
    for histogram in histograms:
        assert histogram.shape == (256, 1)
        assert float(histogram.sum()) == pytest.approx(1.0)


def test_normalized_histograms_are_independent_of_image_resolution():
    image = np.array(
        [
            [[255, 0, 0], [255, 255, 0]],
            [[0, 255, 0], [0, 0, 255]],
        ],
        dtype=np.uint8,
    )
    enlarged = np.tile(image, (3, 4, 1))

    original_histograms = calculate_rgb_histogram(image, normalize=True)
    enlarged_histograms = calculate_rgb_histogram(enlarged, normalize=True)

    for original, scaled in zip(original_histograms, enlarged_histograms, strict=True):
        np.testing.assert_allclose(original, scaled)


def test_default_histograms_preserve_raw_pixel_counts():
    image = np.zeros((2, 3, 3), dtype=np.uint8)

    histograms = calculate_rgb_histogram(image)

    for histogram in histograms:
        assert float(histogram.sum()) == pytest.approx(6.0)
        assert float(histogram[0, 0]) == pytest.approx(6.0)


def test_normalize_flag_must_be_boolean():
    image = np.zeros((2, 2, 3), dtype=np.uint8)

    with pytest.raises(ValueError, match="normalize must be a bool"):
        calculate_rgb_histogram(image, normalize=1)
