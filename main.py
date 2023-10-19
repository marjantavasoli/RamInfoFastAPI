from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ram/{n}")
async def ram_info(n):

    info = [{'free': 1, "used": 2, "total": 3} for i in range(int(n))]
    return info
