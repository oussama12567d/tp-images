

from typing import List
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse


router = APIRouter(
    prefix= "/file",
    tags=["File"],
)


@router.post("/upload_files/", status_code=201)
async def upload_files(files: List[UploadFile] = File(...)):
    try:
        i = 0
        data: dict = {}
        for file in files:
            file.filename = f"input{i}.jpg"
            contents = await file.read()
            with open(f"images/input{i}.jpg", "wb") as f:
                f.write(contents)
            data.update({file.filename: "success"})
            i += 1
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}


@router.post("/upload/", status_code=201)
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


@router.post("/download/", status_code=201)
async def download_image(file_name: str):
    try:
        return FileResponse(path=f"images/{file_name}",)
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An error occurred while processing the file."}
