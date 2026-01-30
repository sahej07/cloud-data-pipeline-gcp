from google.cloud import bigquery

PROJECT_ID = "eastern-moment-358408"
DATASET = "nyc_taxi"
TABLE = "trips_incremental"

# ✅ Correct file that actually exists
GCS_URI = "gs://nyc-taxi-raw-data-sahej/raw/yellow_tripdata_2023-01.csv"

def load_to_bigquery():
    client = bigquery.Client(project=PROJECT_ID)

    table_id = f"{PROJECT_ID}.{DATASET}.{TABLE}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,                  # ✅ FIX
        write_disposition="WRITE_TRUNCATE" # ✅ FIX
    )

    load_job = client.load_table_from_uri(
        GCS_URI,
        table_id,
        job_config=job_config
    )

    load_job.result()
    print("✅ Data loaded into BigQuery successfully")

if __name__ == "__main__":
    load_to_bigquery()
