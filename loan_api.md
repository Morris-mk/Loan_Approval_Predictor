# Loan Prediction API

## What It Does
This API predicts:
- Whether a loan will be approved (`loan_status`: 1 or 0)
- If approved, what amount will be given (`predicted_loan_amount`)

## Input Format (POST to `/predict`)
Send JSON like this:

```json
{
  "person_age": 30,
  "person_income": 45000,
  "person_home_ownership": "RENT",
  "person_emp_length": 5,
  "loan_intent": "PERSONAL",
  "loan_grade": "B",
  "loan_amnt": 10000,
  "loan_int_rate": 12.5,
  "loan_percent_income": 0.22,
  "cb_person_default_on_file": "N",
  "cb_person_cred_hist_length": 7
}
