import numpy as np


def validate_rgb_image(image):
    """Reject invalid RGB arrays with a clear, consistent error."""
    if not isinstance(image, np.ndarray) or image.ndim != 3 or image.shape[2] != 3:
        raise ValueError(
            "Expected an RGB image as a NumPy array with shape "
            "(height, width, 3)."
        )

    if image.shape[0] == 0 or image.shape[1] == 0:
        raise ValueError("RGB image must not be empty.")
