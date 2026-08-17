import cv2

from src.shape.shape_features import extract_shape_features


IMAGE_PATH = "data/sample.jpg"


def test_shape_extraction():
    image, gray, threshold, edges, contours, features = (
        extract_shape_features(IMAGE_PATH)
    )

    assert image is not None
    assert gray is not None
    assert threshold is not None
    assert edges is not None


def test_shape_features():
    image, gray, threshold, edges, contours, features = (
        extract_shape_features(IMAGE_PATH)
    )

    assert isinstance(features, list)

    for feature in features:
        assert "area" in feature
        assert "perimeter" in feature