from fastapi import APIRouter
import functions.function5 as func

router = APIRouter(
    prefix= "/chapter5",
    tags=["Chapter5"],
)




@router.post("/segmentation/detect_and_draw_contours", status_code=201)
async def detect_and_draw_contours(image_path: str):
    try:
        func.detect_and_draw_contours(image_path)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/segmentation/segment_active_contour", status_code=201)
async def segment_active_contour(image_path: str):
    try:
        func.segment_active_contour(image_path)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/segmentation/segment_random_walker", status_code=201)
async def segment_random_walker(image_path: str, seeds: list):
    try:
        func.segment_random_walker(image_path, seeds)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/segmentation/detect_and_draw_circles", status_code=201)
async def detect_and_draw_circles(image_path: str):
    try:
        func.detect_and_draw_circles(image_path)
        return {"filename": "output.jpg", "status": "success"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}