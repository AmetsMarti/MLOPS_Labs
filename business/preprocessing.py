from PIL.Image import Image as ImageType
def resize_image(image: ImageType, height:int, width:int) -> ImageType:
    return image.resize((width, height))
