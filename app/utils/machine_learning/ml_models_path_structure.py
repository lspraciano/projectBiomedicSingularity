from configuration.configs import settings

app_root_path: str = settings.ROOT_PATH_FOR_DYNACONF + "/app"
ml_models_path: str = f"{app_root_path}/utils/machine_learning/ml_models"
detection_path: str = f"{app_root_path}/utils/machine_learning/ml_models/detectors"

ml_models_dict_path_structure: dict = {
    "classification": {
    },
    "detection": {
        "white_blood_cells": {
            "weights_file_name": "white_blood_cells2.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
    },
    "pose": {
    }
}
