# Low-Level Image Feature Extraction

A simple Digital Image Processing (DIP) project demonstrating low-level image feature extraction using Python, OpenCV, NumPy, and Matplotlib.

The project focuses on three basic feature categories:

- **Colour**
- **Texture**
- **Shape**

It also demonstrates how the extracted features can be combined into a single feature vector.

## Project Objectives

The main objective is to understand how visual information in an image can be converted into simple numerical features.

The project follows this pipeline:

```text
                    Input Image
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Colour         Texture         Shape
          │              │              │
      RGB / HSV       Grayscale      Threshold
      Histogram       Statistics         ↓
      Statistics      Histogram         Edges
                                         ↓
                                      Contours
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                Combined Feature Vector
```

## Features Implemented

### Colour Features

- RGB colour representation
- HSV colour representation
- RGB histogram
- Mean
- Minimum
- Maximum

### Texture Features

- Grayscale conversion
- Mean intensity
- Variance
- Standard deviation
- Grayscale histogram

### Shape Features

- Grayscale conversion
- Thresholding
- Canny edge detection
- Contour detection
- Contour area
- Contour perimeter

### Feature Fusion

The project combines colour, texture, and shape values using simple feature concatenation.

## Project Structure

```text
low-level-feature-extraction/
│
├── article/
│   ├── 01-introduction.md
│   ├── 02-low-level-features.md
│   ├── 03-colour-features.md
│   ├── 04-texture-features.md
│   ├── 05-shape-features.md
│   ├── 06-applications.md
│   ├── 07-conclusion.md
│   ├── 08-combining-features.md
│   └── references.md
│
├── data/
│   └── sample.jpg
│
├── examples/
│   ├── colour/
│   ├── texture/
│   ├── shape/
│   └── fusion/
│
├── src/
│   ├── colour/
│   ├── texture/
│   ├── shape/
│   └── fusion/
│
├── tests/
│   ├── test_colour.py
│   ├── test_texture.py
│   ├── test_shape.py
│   └── test_fusion.py
│
├── article/
├── requirements.txt
├── README.md
└── LICENSE
```

## Requirements

- Python 3.10+
- OpenCV
- NumPy
- Matplotlib
- Pytest

## Installation

Clone the repository:

```bash
git clone https://github.com/Chetan-code-lrca/low-level-image-feature-extraction.git
cd low-level-image-feature-extraction
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Examples

### Colour

```bash
python -m examples.colour.colour_features
```

This displays the RGB image, HSV representation, and RGB histogram and prints basic colour statistics.

### Texture

```bash
python -m examples.texture.texture_features
```

This displays the grayscale image and histogram and prints mean, variance, and standard deviation.

### Shape

```bash
python -m examples.shape.shape_features
```

This displays the original image, threshold image, Canny edges, and detected contours.

### Feature Fusion

```bash
python -m examples.fusion.feature_fusion
```

This demonstrates the combination of colour, texture, and shape values into one feature vector.

## Running the Tests

Run the complete test suite:

```bash
python -m pytest -v
```

The project contains tests for:

- Colour feature extraction
- Texture feature extraction
- Shape feature extraction
- Feature fusion

## Applications

Low-level image features can be useful in applications such as:

- Medical image analysis
- Content-Based Image Retrieval (CBIR)
- Object analysis
- Industrial inspection
- Agricultural image analysis
- Remote sensing

## Limitations

This project intentionally uses simple techniques suitable for a basic Digital Image Processing implementation.

It does not currently implement advanced descriptors such as:

- GLCM
- LBP
- Gabor filters
- Advanced shape descriptors
- Machine-learning-based feature extraction

Different images and backgrounds can also affect thresholding, contour detection, and simple statistical measurements.

## Future Work

Possible extensions include:

- GLCM texture features
- Local Binary Patterns (LBP)
- Gabor filters
- More robust shape descriptors
- Feature normalization
- Feature weighting
- Image similarity measurement
- Content-Based Image Retrieval

## Educational Scope

This project is intended as a learning-oriented Digital Image Processing project. The implementations prioritize clarity and understanding of the individual processing steps over advanced optimization.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
