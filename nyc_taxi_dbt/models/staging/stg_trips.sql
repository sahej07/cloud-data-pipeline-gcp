SELECT
  VendorID AS vendor_id,
  tpep_pickup_datetime,
  tpep_dropoff_datetime,
  passenger_count,
  trip_distance,
  fare_amount,
  ingestion_timestamp
FROM {{ source('nyc_taxi', 'trips_incremental') }}
