from pydantic import BaseModel


class WhiteBloodCellWebSocketSchema(BaseModel):
    image_data: str
    reset_persist: bool
