from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import files_endpoint
import chapter1_endpoint

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(files_endpoint.router)
app.include_router(chapter1_endpoint.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}



if __name__ == "__main__":
    config = uvicorn.Config("main:app",host="0.0.0.0", port=10000, log_level="info")
    server = uvicorn.Server(config)
    server.run()