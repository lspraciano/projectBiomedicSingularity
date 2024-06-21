from PIL import Image
from fastapi import UploadFile, HTTPException, status


async def open_valid_image_file(
        file: UploadFile,
):
    try:
        image: Image.Image = Image.open(file.file).convert("RGB")
        return image
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid file. The file must be an image."
        )
