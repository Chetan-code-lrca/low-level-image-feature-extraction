# 4. Texture Feature Extraction

## 4.1 What Is Texture?

Texture describes the visual pattern or variation of intensity within an image.

Examples of textures include:

- Smooth surfaces
- Rough surfaces
- Grass
- Sand
- Fabric
- Wood
- Bricks

Texture is useful because two images can have similar colours but different surface patterns.

## 4.2 Grayscale Representation

For this project, we use a grayscale image for basic texture analysis.

A grayscale image contains intensity values from:

```text
0 → Black
255 → White
```

The grayscale image can be represented as a two-dimensional array of pixel intensities.

```text
Colour Image
     ↓
Grayscale Conversion
     ↓
Intensity Values
     ↓
Texture Statistics
```

Python:

```python
import cv2

image = cv2.imread("data/sample.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

## 4.3 Basic Texture Statistics

A simple way to describe the intensity variation of an image is by using statistical measurements.

In this project, we use:

- Mean
- Variance
- Standard deviation

These measurements provide a simple numerical description of the intensity distribution.

## 4.4 Mean

The mean represents the average intensity of the image.

For an image containing `N` pixels:

\[
\mu = \frac{1}{N}\sum_{i=1}^{N}x_i
\]

where:

- `x_i` is the intensity of a pixel
- `N` is the total number of pixels
- `μ` is the mean intensity

Python:

```python
mean = np.mean(image)
```

A higher mean generally indicates a brighter image, while a lower mean indicates a darker image.

## 4.5 Variance

Variance measures how much the pixel intensities differ from the mean.

\[
\sigma^2 =
\frac{1}{N}\sum_{i=1}^{N}(x_i-\mu)^2
\]

A larger variance indicates greater variation in intensity values.

Python:

```python
variance = np.var(image)
```

## 4.6 Standard Deviation

Standard deviation is the square root of variance.

\[
\sigma = \sqrt{\sigma^2}
\]

Python:

```python
standard_deviation = np.std(image)
```

Standard deviation provides a measure of the spread of intensity values.

## 4.7 Python Implementation

The complete implementation is:

```python
import cv2
import numpy as np

image = cv2.imread("data/sample.jpg", 0)

mean = np.mean(image)
variance = np.var(image)
standard_deviation = np.std(image)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
```

## 4.8 Grayscale Histogram

A histogram shows the distribution of pixel intensity values.

```python
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("data/sample.jpg", 0)

plt.hist(image.ravel(), bins=256, range=[0, 256])

plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.show()
```

The histogram allows us to visually examine how intensity values are distributed throughout the image.

## 4.9 Complete Example

Our implementation combines the grayscale image, histogram, and statistical measurements.

```text
Input Image
     ↓
Grayscale Conversion
     ↓
 ┌───────────────┐
 │               │
 ↓               ↓
Histogram    Statistics
             ├── Mean
             ├── Variance
             └── Standard Deviation
```

The program produces:

1. A grayscale image
2. A grayscale histogram
3. Mean intensity
4. Variance
5. Standard deviation

## 4.10 Interpreting the Results

Suppose an image produces:

```text
Mean               = 118.50
Variance            = 2500.20
Standard Deviation  = 50.00
```

The mean gives an indication of the overall brightness.

Variance and standard deviation indicate how widely the intensity values are distributed.

These measurements provide a simple numerical description of the image's intensity variation.

## 4.11 Applications

Basic texture and intensity statistics can be useful in:

- Image analysis
- Image classification
- Surface inspection
- Medical image analysis
- Agricultural image analysis
- Industrial inspection

For example, industrial inspection can use image-processing measurements to detect differences between acceptable and defective surfaces.

## 4.12 Limitations

Simple statistical measurements have limitations.

They describe the overall intensity distribution but do not fully describe the spatial arrangement of pixels.

For example, two images may have similar mean and variance while having very different spatial patterns.

More advanced texture descriptors can capture spatial relationships, but those techniques are outside the basic scope of this implementation.

## 4.13 Summary

In this section, we implemented a simple texture-analysis approach using:

- Grayscale conversion
- Mean
- Variance
- Standard deviation
- Grayscale histogram

These measurements provide a basic numerical description of intensity variation and form the texture component of our low-level feature extraction project.
