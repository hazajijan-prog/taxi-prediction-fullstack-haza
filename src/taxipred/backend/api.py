from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib

from taxipred.utils.constants import  MODEL_PATH
from taxipred.backend.data_processing import TaxiData, TaxiInput, PredictionOutput

app = FastAPI()
router = APIRouter(prefix="/taxi")

taxi_data = TaxiData()
model = joblib.load(MODEL_PATH)


@router.get("/data")
def read_data():
    return taxi_data.to_json()


@router.post("/predict", response_model=PredictionOutput)
def predict_price(payload: TaxiInput):

    df_input = pd.DataFrame([payload.model_dump()])

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

    prediction = model.predict(df_input)[0]

    return {"predicted_price": prediction}


app.include_router(router)
