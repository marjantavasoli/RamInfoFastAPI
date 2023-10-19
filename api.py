from fastapi import FastAPI
from backend import run_insert_ram_info, get_last_ram_information

app = FastAPI()
run_insert_ram_info(seconds=60)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ram/{number}")
async def ram_info(number):
    return get_last_ram_information(number)
