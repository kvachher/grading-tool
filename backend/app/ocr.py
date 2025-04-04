from fastapi import UploadFile
import os
import requests
import base64
import io

async def process_image(file: UploadFile) -> str:
    """
    Process an image using Google Cloud Vision API
    """
    # Get API key from environment
    api_key = os.getenv("GOOGLE_CLOUD_API_KEY")
    
    # Read the image file
    content = await file.read()
    
    # Encode the image content
    image_content = base64.b64encode(content).decode('utf-8')
    
    # Prepare the request
    url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
    
    # Create the request body
    request_body = {
        "requests": [
            {
                "image": {
                    "content": image_content
                },
                "features": [
                    {
                        "type": "TEXT_DETECTION"
                    }
                ]
            }
        ]
    }
    
    # Make the API request
    response = requests.post(url, json=request_body)
    
    # Parse the response
    if response.status_code == 200:
        result = response.json()
        if result.get("responses") and result["responses"][0].get("textAnnotations"):
            return result["responses"][0]["textAnnotations"][0]["description"]
    
    return ""
