from PIL import Image
from numpy import ndarray
from ultralytics.engine.results import Results, Boxes


def convert_result_to_dict(
        result: Results,
        class_name_list: list
) -> dict:
    output_dict: dict = {
        "class_name_list": [],
        "detect_class_id_list": [],
        "detect_object_confidence_list": [],
        "xyxyn": [],
        "xywhn": [],
    }

    boxes_result: Boxes = result.boxes

    output_dict["class_name_list"] = class_name_list
    output_dict["detect_class_id_list"] = boxes_result.cls.tolist()
    output_dict["detect_object_confidence_list"] = boxes_result.conf.tolist()
    output_dict["xyxyn"] = boxes_result.xyxyn.tolist()
    output_dict["xywhn"] = boxes_result.xywhn.tolist()

    return output_dict


def get_plotted_image_from_result(
        result: Results
) -> Image:
    predict_plotted_array: ndarray = result.plot()
    image_from_array: Image = Image.fromarray(predict_plotted_array[..., ::-1])
    return image_from_array
