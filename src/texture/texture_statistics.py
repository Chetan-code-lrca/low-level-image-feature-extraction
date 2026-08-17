import cv2
import numpy as np


def calculate_texture_statistics(image_path):
    image = cv2.imread(image_path, 0)

    if image is None:
        raise ValueError("Image could not be loaded.")

    mean = np.mean(image)
    variance = np.var(image)
    standard_deviation = np.std(image)

    return {
        "mean": mean,
        "variance": variance,
        "standard_deviation": standard_deviation
    }