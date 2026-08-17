import cv2


def calculate_rgb_histogram(image):
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
