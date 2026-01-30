SELECT
  DATE(tpep_pickup_datetime) AS trip_date,
  COUNT(*) AS total_trips,
  SUM(fare_amount) AS total_fare,
  AVG(trip_distance) AS avg_trip_distance
FROM {{ ref('stg_trips') }}
GROUP BY trip_date
