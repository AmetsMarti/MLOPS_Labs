
import click
from PIL import Image
from business.preprocessing import resize_image


@click.group()
def cli():
    pass

@cli.group()
def preprocessing():
    """Preprocessing module commands"""

@preprocessing.command("resize")
@click.argument(image_path, type = str)
@click.argument(width, type = int)
@click.argument(height, type = int)
def resize_cli(image_path, height, width):
    """Resize a image to size x size"""
    try:
        image = Image.open(image_path)
        click.echo(resize_image(image, width, height))
    except Exception as e:
        click.echo("Error when resizing image: " + str(e))


if __name__ == "__main__":
    cli()
