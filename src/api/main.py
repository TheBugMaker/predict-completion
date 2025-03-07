from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from kedro.io import DataCatalog, Version
from kedro_datasets.pickle import (
    PickleDataset,
)

catalog =  DataCatalog(
    {
        "model": PickleDataset(filepath="data/06_models/model.pickle", version=Version(None, None)),
    }
)
model = catalog.load("model")

# FastAPI app
app = FastAPI(title="ML Model Inference API")

# Request schema
class InputData(BaseModel):
    age: int
    income: float
    employment_type: str
    marital_status: str
    time_spent_on_platform: float
    number_of_sessions: int
    fields_filled_percentage: float
    previous_year_filing: int
    device_type: str
    referral_source: str

# Inference endpoint
@app.post("/predict/")
def predict(data: list[ InputData ]):
    input_data = pd.DataFrame([d.dict() for d in data])
    predictions = model.predict(input_data)  # Get predictions (0 or 1)
    return {"predictions": predictions.tolist()}
