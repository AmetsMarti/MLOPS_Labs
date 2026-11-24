import random

from PIL.Image import Image as ImageType


def make_prediction(image: ImageType) -> str:
    classes = ["buildings", "forest", "glacier", "mountain", "sea", "street"]
    return random.choice(classes)
