from pydantic import BaseModel


class YoloResultSchema(BaseModel):
    detect_class_id_list: list[int] = []
    detect_object_confidence_list: list[float] = []
    xyxyn: list[list[float]] = []
    xywhn: list[list[float]] = []
    class_name_list: dict = []


class YoloTrackResultSchema(YoloResultSchema):
    track_id_list: list[float] = []
