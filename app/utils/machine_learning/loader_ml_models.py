import os

from ultralytics import YOLO

from app.utils.machine_learning.ml_models_path_structure import ml_models_dict_path_structure


def load_yolo_model(
        yolo_model_name: str,
        task: str,
) -> YOLO | None:
    yolo_model_data: dict = ml_models_dict_path_structure[task][yolo_model_name]
    full_ml_model_path: str = f"{yolo_model_data['path']}/{yolo_model_data['weights_file_name']}"

    if not os.path.exists(full_ml_model_path):
        return None

    model: YOLO = YOLO(full_ml_model_path)

    return model
