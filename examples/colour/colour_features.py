import matplotlib.pyplot as plt

from src.colour.rgb_hsv import convert_to_rgb_hsv
from src.colour.histogram import calculate_rgb_histogram
from src.colour.statistics import calculate_rgb_statistics


image_path = "data/sample.jpg"

# Convert image to RGB and HSV
original, rgb, hsv = convert_to_rgb_hsv(image_path)

# Calculate RGB histograms
histograms = calculate_rgb_histogram(rgb)

# Calculate simple colour statistics
statistics = calculate_rgb_statistics(rgb)

print("Colour Statistics:")
for colour, values in statistics.items():
    print(f"{colour}:")
    print(f"  Mean   : {values['mean']:.2f}")
    print(f"  Minimum: {values['minimum']}")
    print(f"  Maximum: {values['maximum']}")

# Display images and histogram
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(rgb)
plt.title("RGB Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(hsv)
plt.title("HSV Image")
plt.axis("off")

plt.subplot(1, 3, 3)

colours = ["red", "green", "blue"]

for i in range(3):
    plt.plot(histograms[i], color=colours[i])

plt.title("RGB Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.tight_layout()
plt.show()