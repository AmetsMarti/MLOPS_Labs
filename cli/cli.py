
import click
from PIL import Image
from business.preprocessing import resize_image
from business.inference import make_prediction


@click.group()
def cli():
    pass

@cli.group()
def preprocessing():
    """Preprocessing module commands"""

@cli.group()
def model():
    "Inference module commands"

@preprocessing.command("resize")
@click.argument("image_path", type = str)
@click.argument("width", type = int)
@click.argument("height", type = int)
def resize_cli(image_path, height, width):
    """Resize a image to size x size"""
    try:
        image = Image.open(image_path)
        click.echo(resize_image(image, width, height))
    except Exception as e:
        click.echo("Error when resizing image: " + str(e))


@model.command("predict")
@click.argument("image_path", type=str)
def make_prediction_cli(image_path):
    "Predict the class of the given image"
    try:
        image = Image.open(image_path)
        click.echo(make_prediction(image))
    except Exception as e:
        click.echo("Error when making prediction " + str(e))


if __name__ == "__main__":
    cli()
