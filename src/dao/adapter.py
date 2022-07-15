from matplotlib import image
import cv2
import numpy as np
from pathlib import Path

class Adapter:

    @staticmethod
    def get_data(image_path: Path) -> np.array:
        img = image.imread(image_path)
        x = cv2.resize(img, (224, 224))
        x = x / 255.0
        x = x[np.newaxis, :]
        return x

