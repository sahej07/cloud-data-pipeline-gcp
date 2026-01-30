import pandas as pd
from datetime import datetime

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
STATE_FILE = "metadata/last_loaded.txt"

def get_last_loaded_timestamp():
    with open(STATE_FILE, "r") as f:
        return pd.to_datetime(f.read().strip())

def update_last_loaded_timestamp(ts):
    with open(STATE_FILE, "w") as f:
        f.write(str(ts))

def download_data():
    df = pd.read_parquet(URL)
    df["ingestion_timestamp"] = datetime.utcnow()

    last_loaded = get_last_loaded_timestamp()
    df = df[df["tpep_pickup_datetime"] > last_loaded]

    if not df.empty:
        update_last_loaded_timestamp(df["tpep_pickup_datetime"].max())

    return df

if __name__ == "__main__":
    df = download_data()
    print(f"New rows loaded: {len(df)}")
