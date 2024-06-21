from functools import lru_cache

from fastapi import HTTPException, status
from ultralytics import YOLO

from app.utils.machine_learning.loader_ml_models import load_yolo_model


def raise_loader_exception(
        ml_model_name: str,
        task: str
) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=[f"Could not load {ml_model_name} model to {task}"]
    )


@lru_cache(maxsize=1)
def wbc_yolo_model_to_detection() -> YOLO:
    yolo_model_name: str = "white_blood_cells"
    task: str = "detection"

    yolo_model: YOLO | None = load_yolo_model(
        yolo_model_name=yolo_model_name,
        task=task,
    )

    if not yolo_model:
        raise raise_loader_exception(
            ml_model_name=yolo_model_name,
            task=task,
        )

    return yolo_model
