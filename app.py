
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Load the trained model
model = joblib.load(BASE_DIR / "diabetes_model.joblib")

# Create FastAPI application
app = FastAPI(title="Diabetes Risk Prediction")

# Configure HTML templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"prediction": None}
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    Pregnancies: int = Form(...),
    Glucose: float = Form(...),
    BloodPressure: float = Form(...),
    SkinThickness: float = Form(...),
    Insulin: float = Form(...),
    BMI: float = Form(...),
    DiabetesPedigreeFunction: float = Form(...),
    Age: int = Form(...)
):
    input_data = pd.DataFrame([{
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }])

    result = int(model.predict(input_data)[0])

    prediction = (
        "Dataset outcome: 1"
        if result == 1
        else "Dataset outcome: 0"
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"prediction": prediction}
    )
