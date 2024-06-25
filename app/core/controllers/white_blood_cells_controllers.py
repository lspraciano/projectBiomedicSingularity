from PIL import Image
from ultralytics import YOLO
from ultralytics.engine.results import Results

from app.core.schemas.yolo_results_schema import YoloResultSchema, YoloTrackResultSchema
from app.utils.machine_learning.results_handler.results_handler import get_plotted_image_from_result, \
    get_yolo_result_schema


async def white_blood_cells_predict(
        white_blood_cells_yolo_model: YOLO,
        image: Image,
        get_plot_image: bool = False,
) -> tuple[Image, YoloResultSchema] | None:
    image_from_array: Image = None
    predict_result_list: list[Results] = white_blood_cells_yolo_model.predict(
        source=image,
        verbose=False,
        conf=0.5
    )
    predict_result: Results = next(iter(predict_result_list))

    if get_plot_image:
        image_from_array: Image = get_plotted_image_from_result(
            result=predict_result
        )

    result_schema: YoloResultSchema = get_yolo_result_schema(
        result=predict_result,
        class_name_list=white_blood_cells_yolo_model.names
    )

    return image_from_array, result_schema


async def white_blood_cells_track(
        white_blood_cells_yolo_model: YOLO,
        image: Image,
        get_plot_image: bool = False,
) -> tuple[Image, YoloResultSchema] | None:
    image_from_array: Image = None
    track_result_list: list[Results] = white_blood_cells_yolo_model.track(
        source=image,
        verbose=False,
        tracker="bytetrack.yaml",
        conf=0.5,
        stream=True
    )

    track_result: Results = next(iter(track_result_list))

    if get_plot_image:
        image_from_array: Image = get_plotted_image_from_result(
            result=track_result
        )

    track_result_schema: YoloTrackResultSchema = get_yolo_result_schema(
        result=track_result,
        class_name_list=white_blood_cells_yolo_model.names,
        is_tracking=True
    )

    return image_from_array, track_result_schema
