import base64
import io
from io import BytesIO

from PIL import Image


def image_to_bytes(
        image: Image
) -> bytes:
    buff: BytesIO = BytesIO()
    image.save(buff, format="JPEG")
    return buff.getvalue()


def base64_to_image(
        base64_str: str
) -> Image.Image:
    image_data: bytes = base64.b64decode(base64_str)
    image: Image = Image.open(io.BytesIO(image_data))
    return image
