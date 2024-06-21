import json
import logging
import time
from typing import Callable

from fastapi import FastAPI, Request, Response
from starlette.responses import StreamingResponse

from app.utils.logger.configure_logger import configure_logger

logger: logging.Logger = configure_logger()


def register_http_logger(app: FastAPI) -> None:
    @app.middleware("http")
    async def api_logging(request: Request, call_next: Callable) -> Response:
        start_time: float = time.time()

        try:
            response: Response | StreamingResponse = await call_next(request)
            content_type: str = response.headers.get("content-type")
            binary_type_list: list[str] = ["image", "application/octet-stream"]
            response_body: bytes = b""
            is_binary: bool = False

            async for chunk in response.body_iterator:
                response_body += chunk

            for binary_type in binary_type_list:
                if binary_type in content_type and content_type:
                    is_binary = True

            if not is_binary:
                try:
                    response_text = response_body.decode()
                except UnicodeDecodeError:
                    response_text = "Failed to decode response as text"
            else:
                response_text = "Response is binary and cannot be logged as text"

            log_message: dict = {
                "status_code": response.status_code,
                "method": request.method,
                "host": request.url.hostname,
                "endpoint": request.url.path,
                "processing_time_seconds": round(time.time() - start_time, 4),
                "response": response_text,
                "headers": dict(request.headers),
            }

            logger.info(msg=log_message)

        except Exception as error:
            logger.error(msg=f"this error needs to be handled: {error} type: {type(error)}")

            return Response(
                status_code=500,
                content=json.dumps({
                    "detail": [
                        "unexpected error. contact support",
                        str(error)
                    ]
                }),
                media_type="application/json"
            )

        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
