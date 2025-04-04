from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ocr import process_image
from app.nlp import grade_text

router = APIRouter()

@router.post("/upload")
async def grade_assignment(file: UploadFile = File(...)):
    # Validate file type (only allow JPEG and PNG)
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a JPEG or PNG image.")
    
    # Extract text using Google Cloud Vision
    extracted_text = await process_image(file)
    if not extracted_text:
        raise HTTPException(status_code=400, detail="Could not extract text from the image.")
    
    # Grade the extracted text using an NLP model (GPT-4 or a Hugging Face model)
    grade_result = await grade_text(extracted_text)
    
    return {
        "text": extracted_text,
        "analysis": grade_result
    }

@router.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy"}
