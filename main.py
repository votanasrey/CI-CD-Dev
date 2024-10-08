from fastapi import APIRouter
import time
from dto import schemas
import pathlib
import uvicorn

app = APIRouter(
    prefix="/api/v1",
    tags=["health-check"]
)

@app.get("/healthz")
async def health_check():
    start = time.time()
    end = time.time()
    return schemas.ResponseData(
        message="success",
        data=True,
        time=(end - start) * 1000
    )

if __name__ == "__main__":
    cwd = pathlib.Path(__file__).parent.resolve()
    uvicorn.run("main:app", host="0.0.0.0", port=8000)