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