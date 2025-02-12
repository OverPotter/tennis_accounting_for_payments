import asyncio
import json
import sys
import time

import httpx
from loguru import logger

LOKI_URL = "http://loki:3100/loki/api/v1/push"


async def send_to_loki(log_dict):
    payload = {
        "streams": [
            {
                "stream": {"job": "tennis_bot"},
                "values": [[str(int(time.time() * 1e9)), json.dumps(log_dict)]],
            }
        ]
    }

    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                LOKI_URL,
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=2,
            )
    except httpx.HTTPError:
        pass


def logger_factory():
    logger.remove()
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | <cyan>{module}</cyan> - <level>{message}</level>"
    )

    logger.add(sys.stdout, format=log_format, level="DEBUG", colorize=True)
    logger.add(
        lambda msg: asyncio.create_task(send_to_loki(msg)),
        serialize=True,
        level="INFO",
    )

    return logger
