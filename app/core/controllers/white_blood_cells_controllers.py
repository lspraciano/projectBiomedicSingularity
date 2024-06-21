from PIL import Image
from ultralytics import YOLO
from ultralytics.engine.results import Results

from app.utils.machine_learning.results_handler.results_handler import get_plotted_image_from_result, \
    convert_result_to_dict


async def white_blood_cells_predict(
        white_blood_cells_yolo_model: YOLO,
        image: Image,
        get_plot_image: bool = False,
) -> tuple[Image, dict] | None:
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

    result_dict: dict = convert_result_to_dict(
        result=predict_result,
        class_name_list=white_blood_cells_yolo_model.names
    )

    return image_from_array, result_dict
