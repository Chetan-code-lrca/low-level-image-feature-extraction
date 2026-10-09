import numpy as np

from src.colour._validation import validate_rgb_image


def calculate_rgb_statistics(image):
    """Return mean, minimum, and maximum for each RGB channel."""
    validate_rgb_image(image)
    statistics = {}

    for i, colour in enumerate(["Red", "Green", "Blue"]):
        channel = image[:, :, i]

        statistics[colour] = {
            "mean": np.mean(channel),
            "minimum": np.min(channel),
            "maximum": np.max(channel)
        }

    return statistics
