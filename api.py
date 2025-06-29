# Import libraries
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy

# load models
clf_model = joblib.load("models\pipeline_clf.pkl")
reg_model = joblib.load("models\pipeline_reg.pkl")

app=FastAPI()

# input schema
class LoanInput(BaseModel):
    person_age: float
    person_income: float
    person_home_ownership: str
    person_emp_length: float
    loan_intent: str
    loan_grade: str
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_default_on_file: str
    cb_person_cred_hist_length: int

@app.post("/predict")
def predict(input: LoanInput):
    data = [input.model_dump()]
    
    # Classification
    status = clf_model.predict(data)[0]
    result = {"loan_status": int(status)}

    # Regression if approved
    if status == 1:
        data[0]["loan_amnt"] = None  # Remove loan_amnt for regressor input
        amount = reg_model.predict(data)[0]
        result["predicted_loan_amount"] = round(float(amount), 2)

    return result
