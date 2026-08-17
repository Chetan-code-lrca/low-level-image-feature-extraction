# 5. Shape Feature Extraction

## 5.1 What Is Shape?

Shape describes the structure or outline of an object in an image.

Shape information can help distinguish objects that may have different boundaries or forms.

Examples include:

- Circular objects
- Rectangular objects
- Irregular objects
- Mechanical parts
- Leaves
- Simple geometric objects

In digital image processing, shape-related features can be obtained from object boundaries or regions.

## 5.2 Grayscale Conversion

Before extracting shape information, the image can be converted into grayscale.

A grayscale image contains intensity values instead of three colour channels.

```python
import cv2

image = cv2.imread("data/sample.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

## 5.3 Thresholding

Thresholding converts a grayscale image into a binary image.

Pixels are divided into two groups according to a threshold value.

In our implementation, the threshold value is `127`.

```python
_, threshold = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)
```

The result contains:

```text
0   → Black
255 → White
```

Thresholding makes it easier to separate objects from the background.

## 5.4 Edge Detection

An edge represents a location where there is a significant change in image intensity.

Edges can provide information about object boundaries.

We use the Canny edge detector provided by OpenCV.

```python
edges = cv2.Canny(gray, 100, 200)
```

The two values specify the lower and upper thresholds used by the Canny operation.

## 5.5 Canny Edge Detection

Canny edge detection is used to identify important edges in an image.

The basic workflow is:

```text
Grayscale Image
       ↓
Canny Edge Detection
       ↓
Edge Image
```

The resulting image contains the detected edges of objects and structures.

## 5.6 Contours

A contour represents the boundary of a connected region or object.

OpenCV provides `findContours()` for detecting contours.

```python
contours, _ = cv2.findContours(
    threshold,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

In this project, `cv2.RETR_EXTERNAL` is used to retrieve the external contours.

The detected contours can then be drawn on the original image.

```python
cv2.drawContours(
    contour_image,
    contours,
    -1,
    (0, 255, 0),
    2
)
```

## 5.7 Area

Contour area represents the area enclosed by a contour.

OpenCV provides `contourArea()`:

```python
area = cv2.contourArea(contour)
```

Area can be used as a simple numerical description of the size of a detected region.

## 5.8 Perimeter

Perimeter represents the length of the contour boundary.

OpenCV provides `arcLength()`:

```python
perimeter = cv2.arcLength(contour, True)
```

The second argument is `True` because the contour is treated as a closed boundary.

## 5.9 Complete Shape Extraction

Our implementation follows:

```text
Input Image
     ↓
Grayscale Conversion
     ↓
Thresholding
     ↓
Edge Detection
     ↓
Contour Detection
     ↓
Area + Perimeter
     ↓
Shape Features
```

The complete implementation is:

```python
import cv2


def extract_shape_features(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    edges = cv2.Canny(gray, 100, 200)

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
```

## 5.10 Example Output

For every detected contour, the program reports:

```text
Contour 1
Area      : ...
Perimeter : ...

Contour 2
Area      : ...
Perimeter : ...
```

The program also displays:

1. Original image
2. Threshold image
3. Canny edge image
4. Image with detected contours

## 5.11 Visualization

The output can be visualized using Matplotlib:

```python
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
```

This makes each stage of shape extraction easy to observe.

## 5.12 Applications

Shape features can be useful in:

- Object detection
- Object classification
- Industrial inspection
- Medical image analysis
- Agriculture
- Character recognition

For example, the area and perimeter of detected regions can help distinguish objects based on their size and boundary.

## 5.13 Limitations

The simple method used in this project has some limitations.

### Dependence on threshold

The quality of the detected contours depends on the selected threshold.

### Complex backgrounds

If the object and background have similar intensities, thresholding may not separate them correctly.

### Multiple objects

An image containing many connected regions can produce many contours.

### Shape changes

Changes in rotation, scale, lighting, or viewpoint can affect the extracted features.

More advanced shape descriptors can provide more robust representations, but they are outside the basic implementation used in this project.

## 5.14 Summary

In this section, we implemented basic shape feature extraction using:

- Grayscale conversion
- Thresholding
- Canny edge detection
- Contour detection
- Contour area
- Contour perimeter

The complete process is:

```text
Image
 ↓
Grayscale
 ↓
Threshold
 ↓
Edges
 ↓
Contours
 ↓
Area + Perimeter
```

These measurements provide simple numerical descriptions of detected object shapes and complete the three basic low-level feature categories used in this project:

```text
Colour
Texture
Shape
```
