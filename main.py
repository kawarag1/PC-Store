from fastapi import FastAPI, HTTPException

import uvicorn

from app.routing.main_router import main_router

app = FastAPI(
    title= "PCStore",
    description="Магазин компьютерной техники",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
app.include_router(main_router)



if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)