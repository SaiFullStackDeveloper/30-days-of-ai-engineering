News Category Classifier API

A Machine Learning project that classifies news text into categories using TF-IDF and Logistic Regression, deployed with FastAPI.

1. Project Setup

Clone the repository and navigate to the project folder.

bash
cd PROJ-AI

2. Activate Virtual Environment

Windows PowerShell:

powershell
.venv\Scripts\activate

3. Install Dependencies
bash
pip install -r requirements.txt

4. Run Automated Tests
bash
pytest -v -s

5. Run FastAPI Application
bash
uvicorn app.main:app --reload

6. Access API Documentation

Open your browser:

Swagger UI: http://127.0.0.1:8000/docs
Health Check: http://127.0.0.1:8000/health
7. Test Prediction API

POST /predict

Request:

json
{
  "text": "NASA launched a new spacecraft"
}


Example response:

json
{
  "prediction": "sci.space"
}

Project Structure
text
PROJ-AI/
├── app/
│   ├── __init__.py
│   └── main.py
├── artifacts/
│   └── classifier.joblib
├── tests/
│   └── test_api.py
├── requirements.txt
└── pytest.ini


Note: Ensure the trained model exists at artifacts/classifier.joblib before running the API or tests.