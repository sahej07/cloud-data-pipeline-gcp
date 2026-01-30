from google.cloud import storage
from ingestion.download_taxi_data import download_data
import pandas as pd

BUCKET_NAME = "nyc-taxi-raw-data-sahej"
DESTINATION_FILE = "raw/yellow_tripdata_incremental.csv"

def upload_to_gcs(df):
    if df.empty:
        print("No new data to upload")
        return

    # 🔹 Select only required columns from NYC Taxi dataset
    df = df[[
        "VendorID",
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "passenger_count",
        "trip_distance",
        "fare_amount"
    ]]

    # 🔹 Rename columns to match BigQuery schema
    df = df.rename(columns={
        "VendorID": "vendor_id"
    })

    # 🔹 Add ingestion timestamp
    df["ingestion_timestamp"] = pd.Timestamp.utcnow()

    # 🔹 Upload clean CSV to GCS
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(DESTINATION_FILE)

    blob.upload_from_string(
        df.to_csv(index=False),
        content_type="text/csv"
    )

    print("Incremental upload complete")

if __name__ == "__main__":
    df = download_data()
    upload_to_gcs(df)
