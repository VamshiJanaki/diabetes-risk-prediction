# Diabetes Risk Prediction

A Machine Learning web application that predicts a class outcome using health-related input measurements. Built with Python, Scikit-learn, FastAPI, HTML, CSS, and Docker.

## Live Demo

**Live Application:** https://diabetes-risk-prediction-4vqk.onrender.com

**GitHub Repository:** https://github.com/VamshiJanaki/diabetes-risk-prediction

## Project Overview

This project demonstrates how a Machine Learning model can be trained on a diabetes dataset and integrated into a web application.

Users can enter health-related measurements into a form and submit them to receive a prediction from the trained model.

## Features

- Machine Learning model using Logistic Regression
- Data preprocessing and missing-value handling
- Interactive web interface built with HTML and CSS
- FastAPI backend for prediction requests
- Docker containerization
- Deployment on Render

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- HTML and CSS
- Docker
- Git and GitHub
- Render

## Input Features

The application accepts these eight inputs:

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. Body Mass Index (BMI)
7. Diabetes Pedigree Function
8. Age

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/VamshiJanaki/diabetes-risk-prediction.git
cd diabetes-risk-prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment on Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
python -m uvicorn app:app --reload
```

### 6. Open the application

Visit http://127.0.0.1:8000 in your browser.

## Run with Docker

Build the Docker image:

```bash
docker build -t diabetes-prediction .
```

Run the container:

```bash
docker run -d -p 8000:8000 --name diabetes-container diabetes-prediction
```

Open http://localhost:8000 in your browser.

## Model Information

The application uses a Logistic Regression model trained on a diabetes dataset. The model processes the input measurements and predicts one of the dataset's two classes.

## Disclaimer

This project is for educational and demonstration purposes only. It is not a medical diagnostic tool. Predictions may be inaccurate and must not be used to make healthcare decisions. Consult a qualified healthcare professional for medical advice.

## Author

**Vamshi Janaki**

GitHub: https://github.com/VamshiJanaki
