from taxipred.utils.constants import CLEANED_TAXI_CSV_PATH
from pydantic import BaseModel, Field
import pandas as pd
import json 

class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(CLEANED_TAXI_CSV_PATH)
        
    def to_json(self):
        return json.loads(self.df.to_json(orient="records"))

class TaxiInput(BaseModel):
    Trip_Distance_km: float = Field(gt=0)
    Time_of_Day: str
    Day_of_Week: str
    Passenger_Count: float
    Traffic_Conditions: str
    Weather: str
    Trip_Duration_Minutes: float = Field(gt=0)

class PredictionOutput(BaseModel): 
    predicted_price: float 
