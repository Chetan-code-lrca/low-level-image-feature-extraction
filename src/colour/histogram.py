import cv2

from src.colour._validation import validate_rgb_image


def calculate_rgb_histogram(image):
    """Return 256-bin histograms for each channel of an RGB image."""
    validate_rgb_image(image)
    histograms = []

    for channel in range(3):
        histogram = cv2.calcHist(
            [image],
            [channel],
            None,
            [256],
            [0, 256]
        )

        histograms.append(histogram)

    return histograms
