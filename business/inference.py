import random

from PIL.Image import Image as ImageType


def resize_image(image: ImageType) -> ImageType:
    return image.resize((224, 224))

def make_prediction(image: ImageType) -> str:
    classes = ["buildings", "forest", "glacier", "mountain", "sea", "street"]
    return random.choice(classes)
