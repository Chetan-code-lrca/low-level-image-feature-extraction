# 2. Understanding Low-Level Image Features

## 2.1 What Are Low-Level Features?

Low-level image features are numerical descriptions derived directly
from the visual information contained in an image.

They generally represent properties such as:

-   Colour
-   Intensity
-   Texture
-   Edges
-   Local patterns
-   Shape

Low-level features differ from high-level semantic information.

For example, a low-level image-processing algorithm may determine that
an image contains:

-   a large number of red pixels,
-   a rough texture,
-   several strong edges, and
-   a roughly circular region.

However, these measurements alone do not necessarily tell the system
that the object is, for example, a **red ball**.

That distinction can be represented as:

``` text
Pixels
  ↓
Low-Level Features
  ↓
Colour / Texture / Shape
  ↓
Higher-Level Interpretation
  ↓
Objects / Scenes / Meaning
```

This project concentrates on the low-level portion of this pipeline.

## 2.2 Colour Features

Colour is one of the most intuitive visual characteristics of an image.

Colour information can first be represented using a **colour space**,
such as:

-   RGB (Red, Green, Blue)
-   HSV (Hue, Saturation, Value)

It is important to distinguish a colour space from a colour feature
descriptor. RGB and HSV define how colour is represented, while
techniques such as **colour histograms** and **colour moments** extract
numerical features from those representations.

### Colour Histogram

A colour histogram describes how frequently different colour or
intensity values occur in an image.

Conceptually:

``` text
Image
  ↓
Select Colour Space / Channel
  ↓
Count Pixel Values
  ↓
Histogram
  ↓
Colour Feature Vector
```

### Colour Moments

Colour moments summarize the statistical distribution of pixel values.

Common moments include:

-   Mean
-   Standard deviation
-   Skewness

These provide a compact alternative to a large histogram.

## 2.3 Texture Features

**Texture** describes spatial patterns and local variations in image
intensity.

Examples of visually different textures include:

-   smooth surfaces,
-   rough surfaces,
-   repeated lines,
-   fabric patterns,
-   grass,
-   brick walls, and
-   biological tissue patterns.

This project investigates three classical texture descriptors.

### Gray-Level Co-occurrence Matrix (GLCM)

GLCM describes how frequently pairs of grayscale values occur at
specified spatial relationships.

Properties derived from a GLCM can include:

-   Contrast
-   Dissimilarity
-   Homogeneity
-   Energy
-   Correlation

### Local Binary Pattern (LBP)

LBP describes local texture by comparing a pixel with its neighbouring
pixels.

A simplified process is:

``` text
Neighbourhood
     ↓
Compare neighbours with centre pixel
     ↓
Binary pattern
     ↓
LBP value
     ↓
LBP histogram
```

### Gabor Filters

Gabor filters respond to image structures at particular frequencies and
orientations. They are useful for detecting directional texture
patterns.

## 2.4 Shape Features

Shape features describe the geometric structure of objects or regions
within an image.

This project investigates several related techniques.

### Edge Detection

Edges represent locations where image intensity changes significantly.
They often correspond to object boundaries or structural details.

### Canny Edge Detection

The Canny method is a widely used multi-stage edge-detection algorithm
involving smoothing, gradient estimation, non-maximum suppression, and
threshold-based edge tracking.

### Contours

Contours represent boundaries of connected objects or regions.

From contours, geometric measurements can be obtained, including:

-   Area
-   Perimeter
-   Centroid
-   Bounding rectangle

### Hu Moments

Hu moments are shape descriptors calculated from image moments. They
provide a compact numerical representation useful for comparing shapes.

## 2.5 What Is a Feature Vector?

A **feature vector** is an ordered collection of numerical feature
values.

For example:

``` text
Colour Feature Vector
[0.20, 0.31, 0.49, 0.12, ...]

Texture Feature Vector
[1.42, 0.83, 0.27, 0.91, ...]

Shape Feature Vector
[0.18, 0.04, 0.002, ...]
```

Different feature vectors can eventually be combined:

``` text
Colour Features
      +
Texture Features
      +
Shape Features
      ↓
Combined Feature Vector
```

Before combining heterogeneous descriptors, normalization is generally
required because the individual features may have very different
numerical ranges.

## 2.6 General Feature-Extraction Pipeline

The complete project will follow this general workflow:

``` text
Input Image
     ↓
Pre-processing
     ↓
Feature Extraction
     ↓
Feature Vectors
     ↓
Normalization
     ↓
Feature Fusion
     ↓
Similarity Measurement
     ↓
Image Retrieval / Analysis
```

Each feature family will initially be implemented and tested
independently.

## 2.7 Why Use Multiple Feature Types?

No single low-level descriptor completely represents every visual
characteristic of an image.

Consider two images with similar overall colours but very different
textures. A colour histogram may consider them similar, while a texture
descriptor may clearly distinguish them.

Likewise:

-   two objects may have similar shapes but different colours;
-   two surfaces may have similar colours but different textures;
-   two images may have similar textures but different object
    boundaries.

Therefore, colour, texture, and shape provide **complementary
information**.

The experimental stage of this project will compare:

  -----------------------------------------------------------------------
  Configuration                       Purpose
  ----------------------------------- -----------------------------------
  Colour only                         Measure the contribution of colour
                                      information

  Texture only                        Measure the contribution of texture
                                      information

  Shape only                          Measure the contribution of
                                      geometric information

  Colour + Texture                    Study complementary appearance
                                      information

  Colour + Shape                      Combine appearance and geometry

  Texture + Shape                     Combine surface patterns and
                                      geometry

  Colour + Texture + Shape            Evaluate the complete low-level
                                      representation
  -----------------------------------------------------------------------

## 2.8 Techniques Used in This Project

The planned implementation is summarized below.

  -----------------------------------------------------------------------
  Category                Representation /        Purpose
                          Technique               
  ----------------------- ----------------------- -----------------------
  Colour                  RGB                     Basic additive colour
                                                  representation

  Colour                  HSV                     Separates hue,
                                                  saturation, and
                                                  brightness information

  Colour                  Colour Histogram        Describes
                                                  colour-frequency
                                                  distribution

  Colour                  Colour Moments          Statistical description
                                                  of colour distribution

  Texture                 GLCM                    Describes spatial
                                                  relationships between
                                                  gray levels

  Texture                 LBP                     Describes local
                                                  neighbourhood patterns

  Texture                 Gabor Filters           Detects oriented and
                                                  frequency-dependent
                                                  textures

  Shape                   Canny                   Extracts significant
                                                  edges

  Shape                   Contours                Represents object
                                                  boundaries

  Shape                   Hu Moments              Produces numerical
                                                  shape descriptors
  -----------------------------------------------------------------------

The following sections implement these techniques individually using
Python, OpenCV, NumPy, scikit-image, SciPy, and Matplotlib.
