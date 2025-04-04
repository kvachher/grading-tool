# Intelligent Grading Tool

An AI-powered grading tool that uses OCR and NLP to grade assignments from images.

## Features

- **OCR Processing**: Extract text from images using Google Cloud Vision API
- **NLP Analysis**: Grade and provide feedback using GPT-4
- **Modern UI**: Clean and intuitive React frontend
- **FastAPI Backend**: Efficient and scalable Python backend

## Tech Stack

- **Frontend**: React, Material-UI
- **Backend**: FastAPI, Python
- **APIs**: Google Cloud Vision, OpenAI GPT-4
- **Database**: PostgreSQL (optional)

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 14+
- Google Cloud Vision API key
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/grading-tool.git
   cd grading-tool
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

4. Create a `.env` file in the backend directory:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_CLOUD_API_KEY=your_google_cloud_api_key
   ```

### Running the Application

1. Start the backend server:
   ```bash
   cd backend
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   python -m uvicorn main:app --reload
   ```

2. Start the frontend server:
   ```bash
   cd frontend
   npm start
   ```

3. Open your browser and navigate to http://localhost:3000

## Usage

1. Upload a JPEG or PNG image containing text
2. The application will extract the text using OCR
3. The extracted text will be analyzed by GPT-4
4. You'll receive a grade and feedback

## Docker Deployment (Optional)

To run the application using Docker:

```bash
docker-compose up --build
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Cloud Vision API for OCR capabilities
- OpenAI for GPT-4 integration
- FastAPI and React communities for excellent frameworks 