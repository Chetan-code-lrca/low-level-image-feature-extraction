import cv2
import matplotlib.pyplot as plt

from src.texture.texture_statistics import calculate_texture_statistics


image_path = "data/sample.jpg"

# Read image in grayscale
image = cv2.imread(image_path, 0)

if image is None:
    raise ValueError("Image could not be loaded.")

# Calculate texture statistics
statistics = calculate_texture_statistics(image_path)

print("Texture Statistics:")
print(f"Mean                : {statistics['mean']:.2f}")
print(f"Variance             : {statistics['variance']:.2f}")
print(f"Standard Deviation   : {statistics['standard_deviation']:.2f}")

# Display grayscale image
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

# Display grayscale histogram
plt.subplot(1, 2, 2)

plt.hist(image.ravel(), bins=256, range=[0, 256])

plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.tight_layout()
plt.show()