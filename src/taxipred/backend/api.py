from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib

from taxipred.utils.constants import CLEANED_TAXI_CSV_PATH, MODEL_PATH
from taxipred.backend.data_processing import TaxiData, TaxiInput, PredictionOutput

app = FastAPI()
router = APIRouter(prefix="/api/taxi/v1")

# Load data + model
taxi_data = TaxiData()
model = joblib.load(MODEL_PATH)


@router.get("/data")
def read_data():
    return taxi_data.to_json()


@router.post("/predict", response_model=PredictionOutput)
def predict_price(payload: TaxiInput):

    # Convert input to DataFrame
    df_input = pd.DataFrame([payload.model_dump()])

    # Match the column order used during model training
    df_input = df_input[
        [
            "Trip_Distance_km",
            "Time_of_Day",
            "Day_of_Week",
            "Passenger_Count",
            "Traffic_Conditions",
            "Weather",
            "Trip_Duration_Minutes",
        ]
    ]

    # Make prediction
    prediction = model.predict(df_input)[0]

    return {"predicted_price": prediction}


app.include_router(router)
