from fastapi import FastAPI
from loguru import logger
import asyncio
import datetime

app = FastAPI()
logger.add("app_logs/requests.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
@app.get("/hello")
async def root():
    # loguru.logger.info("This is a log message")
    await asyncio.sleep(5)
    logger.debug("That's it, beautiful and simple logging!")
    return {"message": "Hello World","now":datetime.datetime.now()}


if __name__ == "__main__":
    logger.info("Starting server...")