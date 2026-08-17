import cv2
import matplotlib.pyplot as plt

from src.shape.shape_features import extract_shape_features


image_path = "data/sample.jpg"

image, gray, threshold, edges, contours, features = (
    extract_shape_features(image_path)
)

# Draw contours on the original image
contour_image = image.copy()

cv2.drawContours(
    contour_image,
    contours,
    -1,
    (0, 255, 0),
    2
)

print("Shape Features:")

for i, feature in enumerate(features):
    print(f"\nContour {i + 1}")
    print(f"Area      : {feature['area']:.2f}")
    print(f"Perimeter : {feature['perimeter']:.2f}")


# Display results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(threshold, cmap="gray")
plt.title("Threshold Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(edges, cmap="gray")
plt.title("Canny Edges")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.title("Contours")
plt.axis("off")

plt.tight_layout()
plt.show()