from taxipred.utils.constants import FINAL_DATA_PATH
from typing import Literal
from pydantic import BaseModel, Field
import pandas as pd
import json 

class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(FINAL_DATA_PATH)
        
    def to_json(self):
        return json.loads(self.df.to_json(orient="records"))

class TaxiInput(BaseModel):
    Trip_Distance_km: float = Field(gt=1, lt=155)
    Time_of_Day: Literal["Morning", "Afternoon", "Evening", "Night"]
    Day_of_Week: Literal["Weekday", "Weekend"]
    Passenger_Count: int = Field(ge=1, le=4)
    Traffic_Conditions: Literal["Low", "Medium", "High"]
    Weather: Literal["Clear", "Rain", "Snow"]
    Trip_Duration_Minutes: float = Field(gt=0)

class PredictionOutput(BaseModel): 
    predicted_price: float 
