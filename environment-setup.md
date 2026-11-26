A Machine Learning project that classifies news text into categories using TF-IDF and Logistic Regression, deployed with FastAPI.

## 1\. Project Setup

Clone the repository and navigate to the project folder.

bash

```bash
cd PROJ-AI
```

## 2\. Activate Virtual Environment

**Windows PowerShell:**

powershell

```powershell
.venv\Scripts\activate
```

## 3\. Install Dependencies

bash

```bash
pip install -r requirements.txt
```

## 4\. Run Automated Tests

bash

```bash
pytest -v -s
```

## 5\. Run FastAPI Application

bash

```bash
uvicorn app.main:app --reload
```

## 6\. Access API Documentation

Open your browser:

- Swagger UI: http://127.0.0.1:8000/docs
- Health Check: http://127.0.0.1:8000/health

## 7\. Test Prediction API

**POST** `/predict`

Request:

json

```json
{
  "text": "NASA launched a new spacecraft"
}
```

Example response:

json

```json
{
  "prediction": "sci.space"
}
```

## Project Structure

text

```text
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
```

**Note:** Ensure the trained model exists at `artifacts/classifier.joblib` before running the API or tests.

One important thing: Make sure your `requirements.txt` includes FastAPI, Uvicorn, scikit-learn, Joblib, pytest and HTTPX. Also, the saved model should be generated using the same compatible scikit-learn version used to load it.