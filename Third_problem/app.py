from pdftozipconverter import PDFScreenshotExtractor
from fastapi import FastAPI,HTTPException
from fastapi import File,UploadFile,BackgroundTasks
from fastapi.responses import FileResponse,PlainTextResponse
import shutil
import os
import tempfile


app=FastAPI()

#asyncronus process and serving pdf
async def process_and_serve_pdf(pdf_file: UploadFile, background_tasks: BackgroundTasks):
    # Save the PDF file temporarily.
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf_file:
        #getting temp file path
        temp_pdf_path = temp_pdf_file.name
        shutil.copyfileobj(pdf_file.file, temp_pdf_file)
    
    zipfilename = f"{tempfile.mktemp()}.zip"
    extracter = PDFScreenshotExtractor(temp_pdf_path, zipfilename)
    extracter.create_zip()
    
    # Serve the zip file
    if os.path.exists(zipfilename):
        return zipfilename
    else:
        return None

@app.post("/process-pdf-image-zip")
async def process_pdf(pdf_file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    zipfilename = await process_and_serve_pdf(pdf_file, background_tasks)
    if zipfilename:
        return FileResponse(zipfilename, media_type="application/zip", filename=zipfilename)
    else:
        return PlainTextResponse("Error: Unable to process PDF", status_code=500)

# cleaning up the files after seding the response pdf as file
@app.post("/cleanup")
async def cleanup_files(background_tasks: BackgroundTasks):
    # Adding cleanup task
    background_tasks.add_task(cleanup_temp_files)
#called after sending response
async def cleanup_temp_files():
    # Cleanup temporary files
    if os.path.exists(temp_pdf_path):
        os.remove(temp_pdf_path)
    if os.path.exists(zipfilename):
        os.remove(zipfilename)
    if hasattr(extracter, 'output_folder') and os.path.exists(extracter.output_folder):
        #remove output folder and its contents
        shutil.rmtree(extracter.output_folder)