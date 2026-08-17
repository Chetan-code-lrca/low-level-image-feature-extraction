# 8. Combining Colour, Texture, and Shape Features

## 8.1 Why Combine Features?

Colour, texture, and shape describe different visual properties of an image.

- **Colour** describes colour information.
- **Texture** describes intensity variation and surface appearance.
- **Shape** describes object boundaries and simple geometric properties.

Using these features together can provide a more complete numerical description of an image.

## 8.2 Feature Combination

The features extracted in the previous sections can be placed into one feature vector.

```text
Colour Features
      +
Texture Features
      +
Shape Features
      ↓
Combined Feature Vector
```

For example:

```text
Colour:
[104.42, 114.93, 118.86]

Texture:
[112.23, 3320.64, 57.63]

Shape:
[1500.00, 180.50]
```

After concatenation:

```text
[104.42, 114.93, 118.86,
 112.23, 3320.64, 57.63,
 1500.00, 180.50]
```

This vector contains information from all three feature categories.

## 8.3 Python Implementation

NumPy can be used to concatenate the feature arrays.

```python
import numpy as np


def combine_features(colour_features, texture_features, shape_features):

    combined_features = np.concatenate([
        np.array(colour_features, dtype=float),
        np.array(texture_features, dtype=float),
        np.array(shape_features, dtype=float)
    ])

    return combined_features
```

## 8.4 Complete Example

```python
from src.fusion.feature_fusion import combine_features


colour_features = [
    104.42,
    114.93,
    118.86
]

texture_features = [
    112.23,
    3320.64,
    57.63
]

shape_features = [
    1500.00,
    180.50
]


combined_features = combine_features(
    colour_features,
    texture_features,
    shape_features
)

print("Colour Features:")
print(colour_features)

print("\nTexture Features:")
print(texture_features)

print("\nShape Features:")
print(shape_features)

print("\nCombined Feature Vector:")
print(combined_features)

print("\nFeature Vector Length:")
print(len(combined_features))
```

Example output:

```text
Colour Features:
[104.42, 114.93, 118.86]

Texture Features:
[112.23, 3320.64, 57.63]

Shape Features:
[1500.0, 180.5]

Combined Feature Vector:
[ 104.42  114.93  118.86  112.23 3320.64   57.63 1500.
  180.5 ]

Feature Vector Length:
8
```

## 8.5 Understanding the Feature Vector

The combined vector has eight values in this example:

```text
3 Colour values
+
3 Texture values
+
2 Shape values
=
8 values
```

The order is:

```text
[Colour, Colour, Colour,
 Texture, Texture, Texture,
 Shape, Shape]
```

Keeping a consistent order is important when using feature vectors for later analysis.

## 8.6 Advantages

Combining features provides several advantages:

- Uses information from multiple visual properties.
- Produces a single numerical representation.
- Can be used as input for later image-analysis tasks.
- Demonstrates how different feature extraction methods can work together.

## 8.7 Limitations

The simple concatenation method used here also has limitations.

Different features may have very different numerical ranges.

For example:

```text
Colour mean       ≈ 100
Texture variance  ≈ 3000
Shape area        ≈ 1500
```

Therefore, the values are not directly comparable in magnitude.

More advanced systems may use feature normalization or weighting before combining features. Those techniques are outside the basic implementation of this project.

## 8.8 Project Feature-Extraction Pipeline

At this stage, our complete project can be represented as:

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

## 8.9 Summary

In this section, we combined the numerical features obtained from:

- Colour
- Texture
- Shape

The process used simple **feature concatenation** to create one combined feature vector.

This demonstrates how independently implemented low-level feature extraction techniques can be brought together into a single representation.
