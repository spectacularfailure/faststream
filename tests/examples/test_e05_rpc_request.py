import pytest

from examples.e05_rpc_request import app, broker, handle
from faststream.rabbit import TestApp, TestRabbitBroker


@pytest.mark.asyncio
async def test_example():
    async with TestRabbitBroker(broker), TestApp(app):
        await handle.wait_call(3)

        handle.mock.assert_called_with("ping")
