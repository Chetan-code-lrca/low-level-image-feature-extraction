import cv2

from examples.sample_image import ensure_sample_image
from src.shape.shape_features import extract_shape_features


IMAGE_PATH = ensure_sample_image()


def test_shape_extraction():
    image, gray, threshold, edges, contours, features = (
        extract_shape_features(IMAGE_PATH)
    )

    assert image is not None
    assert gray is not None
    assert threshold is not None
    assert edges is not None
    assert contours is not None
    assert isinstance(features, dict)


def test_shape_features():
    image, gray, threshold, edges, contours, features = (
        extract_shape_features(IMAGE_PATH)
    )

    assert "contour_count" in features
    assert "total_area" in features
    assert "total_perimeter" in features
    assert features["contour_count"] >= 0
