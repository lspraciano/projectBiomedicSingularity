from PIL import Image
from numpy import ndarray
from ultralytics.engine.results import Results

from app.core.schemas.yolo_results_schema import YoloResultSchema, YoloTrackResultSchema


def get_yolo_result_schema(
        result: Results,
        class_name_list: list,
        is_tracking: bool = False,
) -> YoloResultSchema | YoloTrackResultSchema:
    boxes_result = result.boxes

    if is_tracking:
        track_schema: YoloTrackResultSchema = YoloTrackResultSchema(
            detect_class_id_list=boxes_result.cls.tolist(),
            detect_object_confidence_list=boxes_result.conf.tolist(),
            xyxyn=boxes_result.xyxyn.tolist(),
            xywhn=boxes_result.xywhn.tolist(),
            class_name_list=class_name_list,
            track_id_list=[]
        )

        if hasattr(boxes_result, 'id') and boxes_result.id is not None:
            track_schema.track_id_list = boxes_result.id.cpu().tolist()

        return track_schema

    return YoloResultSchema(
        detect_class_id_list=boxes_result.cls.tolist(),
        detect_object_confidence_list=boxes_result.conf.tolist(),
        xyxyn=boxes_result.xyxyn.tolist(),
        xywhn=boxes_result.xywhn.tolist(),
        class_name_list=class_name_list,
    )


def get_plotted_image_from_result(
        result: Results
) -> Image:
    predict_plotted_array: ndarray = result.plot()
    image_from_array: Image = Image.fromarray(predict_plotted_array[..., ::-1])
    return image_from_array
