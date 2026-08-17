import cv2


def convert_to_rgb_hsv(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded.")

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    return image, rgb, hsv