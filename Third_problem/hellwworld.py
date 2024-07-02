from fastapi import FastAPI,HTTPException
from fastapi import File,UploadFile
from fastapi.responses import FileResponse
import shutil
import os
app=FastAPI()


#for handling root get requests
@app.get("/")
#writing asyncronus function for allowing concurrent execution of code
async def read_root():
    return {
        "Message1":"Sri rama jaya rama jaya jaya rama",
        "Message2":"Sri hanuman jaya hanuman jaya jaya hanuman"    
    }


@app.get("/add")
async def add(a:int,b:int):
    try:
        return {
            "Sum of the given two numbers is ":a+b
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/subtract")
async def subtract_numbers(num1: float, num2: float):
    try:
        result = num1 - num2
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/multiply")
async def multiply_numbers(num1: float, num2: float):
    try:
        result = num1 * num2
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/divide")
async def divide_numbers(num1: float, num2: float):
    try:
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = num1 / num2
        return {"Divison of two numbers": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/process-pdf")
#File(...) is telling fast api to except file from client
#UploadFile class is provided by Fast api for handling file uploads
@app.post("/process_pdf")
async def process_pdf(pdf_file: UploadFile = File(...)):
    try:
        # Save the PDF file temporarily.
        with open("temp.pdf", "wb") as buffer:
            shutil.copyfileobj(pdf_file.file, buffer)

        # Process the file (you can add your logic here).
        # For now, I'm returning the same PDF file.
        return FileResponse("temp.pdf", media_type="application/pdf", filename="pdf_file.pdf")
    except Exception as e:
        return {"error": "Error while processing"}
    finally:
        # os.remove("temp.pdf")
        print("sri rama")


@app.get("/syncrouns_example")
def read_root():
    return {"message": "Hello, world!"}
    