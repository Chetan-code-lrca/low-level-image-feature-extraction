from pathlib import Path

import cv2
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_PATH = PROJECT_ROOT / "data" / "sample.jpg"


def ensure_sample_image() -> str:
    """Create a deterministic sample image when the repository fixture is absent."""
    if SAMPLE_PATH.exists():
        return str(SAMPLE_PATH)

    SAMPLE_PATH.parent.mkdir(parents=True, exist_ok=True)

    image = np.full((160, 160, 3), 245, dtype=np.uint8)
    cv2.rectangle(image, (15, 15), (65, 145), (40, 80, 220), -1)
    cv2.rectangle(image, (95, 20), (145, 135), (60, 190, 80), -1)
    cv2.circle(image, (80, 115), 28, (220, 90, 40), -1)
    cv2.line(image, (10, 150), (150, 10), (30, 30, 30), 3)

    if not cv2.imwrite(str(SAMPLE_PATH), image):
        raise RuntimeError("Could not create the sample image.")

    return str(SAMPLE_PATH)
