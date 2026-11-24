from PIL.Image import Image as ImageType
def resize_image(image: ImageType) -> ImageType:
    return image.resize((224, 224))
