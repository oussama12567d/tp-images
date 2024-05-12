from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import function as func
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload/", status_code=201)
async def upload_image(file: UploadFile = File(...)):
    try:
        file.filename = "input.jpg"
        contents = await file.read()
        with open("images/input.jpg", "wb") as f:
            f.write(contents)
        
        # Return the image as a streaming response
        return {
            "filename": file.filename,
            "status": "success",
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}

@app.post("/download/", status_code=201)
async def download_image():
    try:
        return FileResponse(path="images/output.jpg")
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}
    

@app.post("/rotate_image/", status_code=201)
async def rotate_image(angle: int):
    try:
        func.rotate_image("images/input.jpg", angle)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@app.post("/scale_image/", status_code=201)
async def scale_image(scale_x: float, scale_y: float):
    try:
        func.scale_image("images/input.jpg", scale_x, scale_y)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)