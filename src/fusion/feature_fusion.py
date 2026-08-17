import numpy as np


def combine_features(colour_features, texture_features, shape_features):
    """Combine colour, texture, and shape features."""

    combined_features = np.concatenate([
        np.array(colour_features, dtype=float),
        np.array(texture_features, dtype=float),
        np.array(shape_features, dtype=float)
    ])

    return combined_features