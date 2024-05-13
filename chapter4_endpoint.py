from fastapi import APIRouter
import functions.function4 as func

router = APIRouter(
    prefix= "/chapter4",
    tags=["Chapter4"],
)


@router.post("/image_enhancement/apply_clahe", status_code=201)
async def apply_clahe():
    try:
        func.apply_clahe("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/image_enhancement/linear_contrast_stretching", status_code=201)
async def linear_contrast_stretching():
    try:
        func.linear_contrast_stretching("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/image_enhancement/mean_filter", status_code=201)
async def mean_filter(value: int):
    try:
        func.mean_filter("images/input.jpg", value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/image_enhancement/median_filter", status_code=201)
async def median_filter(value: int):
    try:
        func.median_filter("images/input.jpg", value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/image_enhancement/bilateral_filter", status_code=201)
async def bilateral_filter(d: int, sigmaColor: int, sigmaSpace: int):
    try:
        func.bilateral_filter("images/input.jpg", d, sigmaColor, sigmaSpace)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/image_enhancement/unsharp_masking", status_code=201)
async def unsharp_masking(amount: int = 1.5, radius: int = 5):
    try:
        func.unsharp_masking("images/input.jpg", amount, radius)
        return {"filename": "output.jpg", "status": "success"}  
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/image_enhancement/adjust_white_balance", status_code=201)
async def adjust_white_balance():
    try:
        func.adjust_white_balance("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/image_restoration/add_gaussian_noise", status_code=201)
async def add_gaussian_noise(mean: int = 0, stddev: int = 20):
    try:
        func.add_gaussian_noise("images/input.jpg", mean, stddev)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/image_restoration/apply_gaussian_blur", status_code=201)
async def apply_gaussian_blur(kernel_size: int = 5):
    try:
        func.apply_gaussian_blur("images/input.jpg", kernel_size)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/image_restoration/downsample", status_code=201)
async def downsample(scale_factor: int = 2):
    try:
        func.downsample("images/input.jpg", scale_factor)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}

