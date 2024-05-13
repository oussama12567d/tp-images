from fastapi import APIRouter
import functions.function2 as func

router = APIRouter(
    prefix= "/chapter2",
    tags=["Chapter2"],
)


@router.post("/arithmetic_transformations/adjust_brightness", status_code=201)
async def adjust_brightness(addition_value: int):
    try:
        func.adjust_brightness("images/input.jpg", addition_value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/arithmetic_transformations/adjust_brightness_subtract", status_code=201)
async def adjust_brightness_subtract(subtraction_value: int):
    try:
        func.adjust_brightness_subtract("images/input.jpg", subtraction_value)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/arithmetic_transformations/adjust_contrast", status_code=201)
async def adjust_contrast(multiplication_factor: float):
    try:
        func.adjust_contrast("images/input.jpg", multiplication_factor)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}
