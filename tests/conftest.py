import asyncio
from asyncio import AbstractEventLoop
from typing import AsyncIterator, Iterator

import pytest as pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.main import app
from configuration.configs import settings


@pytest_asyncio.fixture(
    scope="module"
)
async def async_client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(
            app=app,
            base_url=f"http://{settings.API_URL}"
    ) as client, LifespanManager(app):
        yield client


@pytest.fixture(
    scope="session"
)
def event_loop() -> Iterator[AbstractEventLoop]:
    loop: AbstractEventLoop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
