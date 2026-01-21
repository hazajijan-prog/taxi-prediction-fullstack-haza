from pathlib import Path 

DATA_PATH = Path(__file__).parents[1] / "data"
TAXI_CSV_PATH = DATA_PATH / "taxi_trip_pricing.csv"

CLEANED_TAXI_CSV_PATH = DATA_PATH / "taxi_trip_clean.csv"
MODEL_PATH = DATA_PATH / "final_model.joblib"

FINAL_DATA_PATH = DATA_PATH / "final_data.csv"