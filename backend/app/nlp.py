import openai
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

async def grade_text(extracted_text: str) -> dict:
    prompt = (
        f"Please grade the following assignment answer and provide detailed feedback:\n\n{extracted_text}"
    )
    
    try:
        # Run the OpenAI API call in an executor to avoid blocking
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a teaching assistant grading an assignment."},
                    {"role": "user", "content": prompt},
                ],
            )
        )
        
        grade = response.choices[0].message['content']
        return {"grade": grade, "status": "success"}
    except Exception as e:
        return {"error": str(e), "status": "error"}
