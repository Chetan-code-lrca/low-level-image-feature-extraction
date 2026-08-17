# 7. Conclusion

This project studied and implemented basic **low-level image feature extraction** techniques using Python and OpenCV.

The project focused on three major categories:

```text
Low-Level Image Features
│
├── Colour
├── Texture
└── Shape
```

## 7.1 Colour Features

The colour section implemented:

- RGB colour representation
- HSV colour representation
- RGB colour histogram
- Mean
- Minimum
- Maximum

These features provide a simple numerical description of colour information in an image.

## 7.2 Texture Features

The texture section used a grayscale image and calculated:

- Mean
- Variance
- Standard deviation
- Grayscale histogram

These measurements provide a basic description of intensity variation.

## 7.3 Shape Features

The shape section implemented:

- Grayscale conversion
- Thresholding
- Canny edge detection
- Contour detection
- Contour area
- Contour perimeter

These operations provide simple information about the boundaries and size of detected regions.

## 7.4 Overall Pipeline

The complete project can be summarized as:

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
                 Image Features
```

## 7.5 What Was Learned

Through this implementation, the following concepts were demonstrated:

- How images are represented digitally
- How colour information can be extracted
- How histograms describe pixel distributions
- How grayscale intensity statistics can describe an image
- How thresholding can separate regions
- How edges can reveal object boundaries
- How contours can be used to measure simple shape properties

The implementations were intentionally kept simple so that each processing step can be understood and reproduced using basic Digital Image Processing concepts.

## 7.6 Future Extension

The project can later be extended with more advanced feature descriptors and image-retrieval techniques.

Possible extensions include:

- GLCM texture features
- Local Binary Patterns
- More advanced shape descriptors
- Feature normalization
- Combining colour, texture, and shape features
- Image similarity measurement
- Content-Based Image Retrieval

These extensions are outside the basic implementation presented here.
