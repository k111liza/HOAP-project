import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Подключение каталога "uploads" для хранения загруженных файлов
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.post("/uploadfile/{file_name}")
async def create_upload_file(file: UploadFile = File(...), file_name : str = ""):
    file_name+='.pdf'
    file_path = os.path.join("uploads", file_name)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}

@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = os.path.join("uploads", file_name)
    return FileResponse(file_path, filename=file_name)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)