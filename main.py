from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import uvicorn
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


@app.post("/translate_image/", status_code=201)
async def translate_image(tx: int, ty: int):
    try:
        func.translate_image("images/input.jpg", tx, ty)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@app.post("/horizontal_reflection/", status_code=201)
async def horizontal_reflection():
    try:
        func.horizontal_reflection("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@app.post("/affine_transform/", status_code=201)
async def affine_transform(scale_x: float, scale_y: float, shear_x: int, shear_y: int, translation_x: int, translation_y: int):
    try:
        func.affine_transform("images/input.jpg",scale_x, scale_y, shear_x, shear_y, translation_x, translation_y)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@app.post("/adjust_brightness/", status_code=201)
async def adjust_brightness(addition_value: int):
    try:
        func.adjust_brightness("images/input.jpg", addition_value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/adjust_brightness_subtract/", status_code=201)
async def adjust_brightness_subtract(subtraction_value: int):
    try:
        func.adjust_brightness_subtract("images/input.jpg", subtraction_value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/adjust_contrast/", status_code=201)
async def adjust_contrast(multiplication_factor: float):
    try:
        func.adjust_contrast("images/input.jpg", multiplication_factor)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/bitwise_and_images/", status_code=201)
async def bitwise_and_images(image_path1: str, image_path2: str):
    try:
        func.bitwise_and_images(image_path1, image_path2)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@app.post("/apply_thresholding/", status_code=201)
async def apply_thresholding(threshold_value: int):
    try:
        func.apply_thresholding("images/input.jpg", threshold_value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/apply_gaussian_blur/", status_code=201)
async def apply_gaussian_blur():
    try:
        func.apply_gaussian_blur("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/apply_laplacian_filter/", status_code=201)
async def apply_laplacian_filter():
    try:
        func.apply_laplacian_filter("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/apply_sobel_filter/", status_code=201)
async def apply_sobel_filter():
    try:
        func.apply_sobel_filter("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/apply_bandpass_filter/", status_code=201)
async def apply_bandpass_filter():
    try:
        func.apply_bandpass_filter("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}




@app.post("/apply_custom_filter/", status_code=201)
async def apply_custom_filter(custom_kernel: object = [[0, -1, 0],[-1, 5, -1],[0, -1, 0]]):
    try:
        func.apply_custom_filter("images/input.jpg", custom_kernel)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/perform_spatial_convolution/", status_code=201)
async def perform_spatial_convolution(kernel_size: int):
    try:
        func.perform_spatial_convolution("images/input.jpg", kernel_size)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/contrast_stretching/", status_code=201)
async def contrast_stretching():
    try:
        func.contrast_stretching("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/histogram_equalization/", status_code=201)
async def histogram_equalization():
    try:
        func.histogram_equalization("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@app.post("/histogram_equalization_opencv/", status_code=201)
async def histogram_equalization_opencv():
    try:
        func.histogram_equalization_opencv("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


if __name__ == "__main__":
    config = uvicorn.Config("main:app",host="0.0.0.0", port=10000, log_level="info")
    server = uvicorn.Server(config)
    server.run()