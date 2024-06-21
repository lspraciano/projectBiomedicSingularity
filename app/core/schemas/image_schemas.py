from pydantic import BaseModel


class ImageResponseSchema(BaseModel):
    file_data: bytes


image_response_200: dict = {
    200: {
        "content": {
            "image/jpeg": {}
        },
        "description": "Return an image in body and the detections in headers key 'Detections' ",
    },
}
