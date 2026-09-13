# Low-Level Image Feature Extraction

A small Digital Image Processing project that turns an image into simple numerical features for colour, texture, and shape.

The project is written in Python and uses OpenCV, NumPy, and Matplotlib. Each feature type is implemented separately and then combined into a single feature vector.

## What it covers

### Colour

- RGB and HSV representations
- RGB histograms
- Mean, minimum, and maximum channel values

### Texture

- Grayscale conversion
- Mean intensity
- Variance
- Standard deviation
- Grayscale histogram

### Shape

- Grayscale conversion
- Thresholding
- Canny edge detection
- Contour detection
- Contour area and perimeter

### Feature fusion

The colour, texture, and shape outputs are concatenated into one feature vector that can be used as input to a later analysis or machine-learning step.

## Processing pipeline

```text
Input image
    │
    ├── Colour  ──> RGB / HSV statistics + histogram
    │
    ├── Texture ─> Grayscale statistics + histogram
    │
    └── Shape   ─> Threshold -> Edges -> Contours
                       │
                       ▼
              Combined feature vector
```

## Repository layout

```text
low-level-image-feature-extraction/
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
├── data/
│   └── sample.jpg
├── examples/
│   ├── colour/
│   ├── texture/
│   ├── shape/
│   └── fusion/
├── src/
│   ├── colour/
│   ├── texture/
│   ├── shape/
│   └── fusion/
├── tests/
│   ├── test_colour.py
│   ├── test_texture.py
│   ├── test_shape.py
│   └── test_fusion.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Requirements

- Python 3.10 or newer
- OpenCV
- NumPy
- Matplotlib
- Pytest

The repository's `requirements.txt` is a full captured Python environment and includes Jupyter-related packages as well as the image-processing dependencies. The commands below are enough to install everything it specifies.

## Setup

Clone the repository:

```bash
git clone https://github.com/Chetan-code-lrca/low-level-image-feature-extraction.git
cd low-level-image-feature-extraction
```

Create a virtual environment.

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the examples

The examples operate on the sample image in `data/sample.jpg`.

### Colour features

```bash
python -m examples.colour.colour_features
```

This shows the RGB image, HSV representation, and RGB histogram and prints basic colour statistics.

### Texture features

```bash
python -m examples.texture.texture_features
```

This converts the image to grayscale, displays the grayscale image and histogram, and prints the mean, variance, and standard deviation.

### Shape features

```bash
python -m examples.shape.shape_features
```

This shows the thresholded image, Canny edges, and detected contours and reports contour measurements.

### Feature fusion

```bash
python -m examples.fusion.feature_fusion
```

This combines the colour, texture, and shape outputs into one feature vector.

## Run the tests

```bash
python -m pytest -v
```

The test suite covers the colour, texture, shape, and fusion modules.

## Notes on the implementation

The project deliberately uses simple, easy-to-follow image statistics rather than advanced descriptors. That makes it useful for understanding how raw pixel information can be turned into features before moving on to more complex computer-vision pipelines.

Thresholding and contour detection are sensitive to image content and background conditions, so the results can change substantially between images.

## Possible extensions

Natural next steps include:

- GLCM-based texture features
- Local Binary Patterns (LBP)
- Gabor filters
- More robust shape descriptors
- Feature normalization and weighting
- Image similarity and retrieval
- A classifier built on the combined feature vectors

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
