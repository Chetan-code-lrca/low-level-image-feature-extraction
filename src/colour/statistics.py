import numpy as np


def calculate_rgb_statistics(image):
    statistics = {}

    for i, colour in enumerate(["Red", "Green", "Blue"]):
        channel = image[:, :, i]

        statistics[colour] = {
            "mean": np.mean(channel),
            "minimum": np.min(channel),
            "maximum": np.max(channel)
        }

    return statistics
