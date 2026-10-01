import cv2

from examples.sample_image import ensure_sample_image
from src.texture.texture_statistics import calculate_texture_statistics


IMAGE_PATH = ensure_sample_image()


def test_texture_statistics():
    statistics = calculate_texture_statistics(IMAGE_PATH)

    assert "mean" in statistics
    assert "variance" in statistics
    assert "standard_deviation" in statistics


def test_grayscale_image():
    image = cv2.imread(IMAGE_PATH, 0)

    assert image is not None
    assert len(image.shape) == 2
