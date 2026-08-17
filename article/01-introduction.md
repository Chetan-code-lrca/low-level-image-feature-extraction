# 1. Introduction

Digital Image Processing (DIP) is the use of computational techniques to
process, analyze, enhance, and extract useful information from digital
images.

A digital image is fundamentally represented by pixel values. Although
these pixels contain the complete visual information of an image,
directly comparing or analyzing millions of individual pixel values is
often inefficient and does not provide a compact description of the
image. **Feature extraction** addresses this problem by transforming
visual characteristics into meaningful numerical descriptors.

## 1.1 What Is an Image Feature?

An **image feature** is a measurable property or characteristic obtained
from an image.

Common examples include:

-   Colour
-   Texture
-   Shape
-   Edges
-   Corners
-   Local intensity patterns

A feature-extraction algorithm converts these characteristics into
numerical values known collectively as a **feature vector**.

``` text
Input Image
     ↓
Feature Extraction
     ↓
Feature Vector
[0.12, 0.35, 0.81, 0.42, ...]
```

The resulting feature vector can be used for image comparison,
retrieval, classification, recognition, and other image-processing
tasks.

## 1.2 Low-Level Image Features

**Low-level features** describe visual properties that can be derived
directly from image pixels without requiring semantic understanding of
the objects or scene.

This project focuses on three major categories:

1.  **Colour features**
2.  **Texture features**
3.  **Shape features**

Each category captures a different aspect of visual information.

-   **Colour** describes the distribution and statistical
    characteristics of colours.
-   **Texture** describes repeated patterns, local intensity variations,
    and surface appearance.
-   **Shape** describes boundaries and geometric characteristics of
    objects or regions.

These features are complementary. Combining them can provide a richer
description than relying on a single feature type.

## 1.3 Why Is Feature Extraction Necessary?

A raw image may contain hundreds of thousands or millions of pixel
values. Working directly with all pixels can be computationally
expensive and may make meaningful image comparison difficult.

Feature extraction provides a more compact representation:

``` text
Raw Image
   ↓
Relevant Visual Information
   ↓
Numerical Descriptors
   ↓
Compact Feature Vector
```

This representation can make image analysis and comparison more
efficient.

## 1.4 Applications

Classical low-level image features have applications in areas including:

-   Content-Based Image Retrieval (CBIR)
-   Object recognition
-   Medical image analysis
-   Remote sensing
-   Industrial inspection
-   Agricultural image analysis
-   Image classification
-   Pattern recognition

## 1.5 Project Objective

The objective of this Digital Image Processing project is to **study,
implement, visualize, and experimentally compare classical low-level
image feature extraction techniques using Python**.

The project will investigate:

``` text
Low-Level Image Features
│
├── Colour
│   ├── RGB and HSV colour spaces
│   ├── Colour Histograms
│   └── Colour Moments
│
├── Texture
│   ├── Gray-Level Co-occurrence Matrix (GLCM)
│   ├── Local Binary Pattern (LBP)
│   └── Gabor Filters
│
└── Shape
    ├── Edge Detection
    ├── Canny Edge Detection
    ├── Contours
    └── Hu Moments
```

After implementing the individual descriptors, the project will study
feature normalization, feature fusion, similarity measurement, and image
retrieval.

## 1.6 Final Project Goal

The final system will follow the general architecture:

``` text
                       Input Image
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
           Colour        Texture        Shape
           Features      Features      Features
              │             │             │
              └─────────────┼─────────────┘
                            ↓
                     Normalization
                            ↓
                      Feature Fusion
                            ↓
                  Combined Feature Vector
                            ↓
                   Similarity Measurement
                            ↓
                  Similar-Image Retrieval
```

The experiments will also compare colour-only, texture-only, shape-only,
and combined feature representations to understand the strengths and
limitations of each approach.
