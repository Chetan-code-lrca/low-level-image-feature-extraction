import cv2


def extract_shape_features(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Find contours
    contours, _ = cv2.findContours(
        threshold,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    features = []

    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        features.append({
            "area": area,
            "perimeter": perimeter
        })

    return image, gray, threshold, edges, contours, features