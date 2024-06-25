import torch
from PIL import Image
from fastapi import APIRouter, status, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse
from pydantic_core._pydantic_core import ValidationError
from ultralytics import YOLO

from app.core.controllers.white_blood_cells_controllers import white_blood_cells_predict, white_blood_cells_track
from app.core.dependencies.images.images import open_valid_image_file
from app.core.dependencies.machine_learning.ml_models_loader import wbc_yolo_model_to_detection
from app.core.schemas.image_schemas import ImageResponseSchema, image_response_200
from app.core.schemas.white_blood_cells_schemas import WhiteBloodCellWebSocketSchema
from app.core.schemas.yolo_results_schema import YoloResultSchema, YoloTrackResultSchema
from app.utils.images_handler.images_handler import image_to_bytes, base64_to_image

router = APIRouter(
    tags=["White Blood Cells"],
    prefix="/white-blood-cells"
)


@router.post(
    path="/predict",
    response_class=StreamingResponse,
    response_model=ImageResponseSchema,
    responses=image_response_200,
    status_code=status.HTTP_200_OK
)
async def complete_predict_(
        image: Image = Depends(open_valid_image_file),
        blood_serum_yolo_model: YOLO = Depends(wbc_yolo_model_to_detection)
):
    result_image: Image
    result_schema: YoloResultSchema

    result_image, result_schema = await white_blood_cells_predict(
        white_blood_cells_yolo_model=blood_serum_yolo_model,
        image=image,
        get_plot_image=True
    )

    response: StreamingResponse = StreamingResponse(
        content=iter([image_to_bytes(result_image)]),
        media_type=f"image/{result_image.format}"
    )

    response.headers["Detections"]: str = result_schema.model_dump_json()

    return response


@router.websocket("/track/ws")
async def track_ws_(
        websocket: WebSocket,
        blood_serum_yolo_model: YOLO = Depends(wbc_yolo_model_to_detection)
):
    device: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    await websocket.accept()

    try:
        result_image: Image
        result_schema: YoloTrackResultSchema

        if blood_serum_yolo_model.predictor:
            blood_serum_yolo_model.predictor.trackers[0].reset()

        while True:
            data_from_websocket: str = await websocket.receive_text()
            request_json: WhiteBloodCellWebSocketSchema = WhiteBloodCellWebSocketSchema.parse_raw(
                data_from_websocket
            )
            image_data: str = request_json.image_data

            if request_json.reset_persist:
                blood_serum_yolo_model.predictor.trackers[0].reset()

            if image_data.startswith("data:image/jpeg;base64,"):
                base64_str: str = image_data.split(",", 1)[1]
                image: Image = base64_to_image(base64_str)
                result_image, result_schema = await white_blood_cells_track(
                    white_blood_cells_yolo_model=blood_serum_yolo_model,
                    image=image,
                    device=device
                )

                if result_image:
                    image_bytes: bytes = image_to_bytes(result_image)
                    await websocket.send_bytes(image_bytes)
                await websocket.send_text(result_schema.model_dump_json())
            else:
                await websocket.close(
                    code=1003,
                    reason="Invalid data format"
                )
    except WebSocketDisconnect:
        print("Client disconnected")
    except ValidationError:
        await websocket.close(
            code=1003,
            reason="Invalid JSON format"
        )
    except Exception as error:
        print(f"Unexpected error: {error}")
