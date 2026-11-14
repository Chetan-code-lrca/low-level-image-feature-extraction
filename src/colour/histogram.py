import cv2

from src.colour._validation import validate_rgb_image


def calculate_rgb_histogram(image, normalize=False):
    """Return 256-bin histograms for each RGB channel.

    By default, bins contain raw pixel counts for backwards compatibility.
    Set normalize=True to return per-pixel frequencies whose sum is 1 for
    each channel, making histograms comparable across image resolutions.
    """
    validate_rgb_image(image)
    if not isinstance(normalize, bool):
        raise ValueError("normalize must be a bool")

    pixel_count = float(image.shape[0] * image.shape[1])
    histograms = []

    for channel in range(3):
        histogram = cv2.calcHist(
            [image],
            [channel],
            None,
            [256],
            [0, 256],
        )
        if normalize:
            histogram /= pixel_count
        histograms.append(histogram)

    return histograms
