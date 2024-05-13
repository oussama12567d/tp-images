from fastapi import APIRouter
import functions.function3 as func

router = APIRouter(
    prefix= "/chapter3",
    tags=["Chapter3"],
)


@router.post("/contrast_stretching/contrast_stretching", status_code=201)
async def contrast_stretching():
    try:
        func.contrast_stretching("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/convolution/perform_spatial_convolution", status_code=201)
async def perform_spatial_convolution(value: int):
    try:
        func.perform_spatial_convolution("images/input.jpg", value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/filtre/low_pass", status_code=201)
async def low_pass(value: int = 5):
    try:
        func.low_pass("images/input.jpg", value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}
    

@router.post("/filtre/high_pass", status_code=201)
async def high_pass():
    try:
        func.high_pass("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}
    

@router.post("/filtre/band_pass", status_code=201)
async def band_pass(kernel_size: int = 5):
    try:
        func.Band_pass("images/input.jpg", kernel_size)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/filtre/apply_custom_filter", status_code=201)
async def apply_custom_filter(value: list = [[0, -1, 0], [-1, 5, -1],[0, -1, 0]]):
    try:
        func.apply_custom_filter("images/input.jpg", value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/map_pixel_intensities/histogram_equalization", status_code=201)
async def histogram_equalization():
    try:
        func.histogram_equalization("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/map_pixel_intensities/contrast_stretching", status_code=201)
async def contrast_stretching():
    try:
        func.contrast_stretching("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/transformer_de_fourier/apply_gaussian_blur", status_code=201)
async def apply_gaussian_blur(kernel_size: int = 5):
    try:
        func.apply_gaussian_blur("images/input.jpg", kernel_size)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}
