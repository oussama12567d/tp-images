from fastapi import APIRouter
import functions.function1 as func

router = APIRouter(
    prefix= "/chapter1",
    tags=["Chapter1"],
)





@router.post("/rotate_image/", status_code=201)
async def rotate_image(angle: int):
    try:
        func.rotate_image("images/input.jpg", angle)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/scale_image/", status_code=201)
async def scale_image(scale_x: float, scale_y: float):
    try:
        func.scale_image("images/input.jpg", scale_x, scale_y)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/translate_image/", status_code=201)
async def translate_image(tx: int, ty: int):
    try:
        func.translate_image("images/input.jpg", tx, ty)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/horizontal_reflection/", status_code=201)
async def horizontal_reflection():
    try:
        func.horizontal_reflection("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/affine_transform/", status_code=201)
async def affine_transform(scale_x: float, scale_y: float, shear_x: int, shear_y: int, translation_x: int, translation_y: int):
    try:
        func.affine_transform("images/input.jpg",scale_x, scale_y, shear_x, shear_y, translation_x, translation_y)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/adjust_brightness/", status_code=201)
async def adjust_brightness(addition_value: int):
    try:
        func.adjust_brightness("images/input.jpg", addition_value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/adjust_brightness_subtract/", status_code=201)
async def adjust_brightness_subtract(subtraction_value: int):
    try:
        func.adjust_brightness_subtract("images/input.jpg", subtraction_value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/adjust_contrast/", status_code=201)
async def adjust_contrast(multiplication_factor: float):
    try:
        func.adjust_contrast("images/input.jpg", multiplication_factor)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/bitwise_and_images/", status_code=201)
async def bitwise_and_images(image_path1: str, image_path2: str):
    try:
        func.bitwise_and_images(image_path1, image_path2)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/routerly_thresholding/", status_code=201)
async def routerly_thresholding(threshold_value: int):
    try:
        func.routerly_thresholding("images/input.jpg", threshold_value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/routerly_gaussian_blur/", status_code=201)
async def routerly_gaussian_blur():
    try:
        func.routerly_gaussian_blur("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/routerly_laplacian_filter/", status_code=201)
async def routerly_laplacian_filter():
    try:
        func.routerly_laplacian_filter("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/routerly_sobel_filter/", status_code=201)
async def routerly_sobel_filter():
    try:
        func.routerly_sobel_filter("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/routerly_bandpass_filter/", status_code=201)
async def routerly_bandpass_filter():
    try:
        func.routerly_bandpass_filter("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}




@router.post("/routerly_custom_filter/", status_code=201)
async def routerly_custom_filter(custom_kernel: object = [[0, -1, 0],[-1, 5, -1],[0, -1, 0]]):
    try:
        func.routerly_custom_filter("images/input.jpg", custom_kernel)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/perform_spatial_convolution/", status_code=201)
async def perform_spatial_convolution(kernel_size: int):
    try:
        func.perform_spatial_convolution("images/input.jpg", kernel_size)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/contrast_stretching/", status_code=201)
async def contrast_stretching():
    try:
        func.contrast_stretching("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/histogram_equalization/", status_code=201)
async def histogram_equalization():
    try:
        func.histogram_equalization("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}



@router.post("/histogram_equalization_opencv/", status_code=201)
async def histogram_equalization_opencv():
    try:
        func.histogram_equalization_opencv("images/input.jpg")
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}
