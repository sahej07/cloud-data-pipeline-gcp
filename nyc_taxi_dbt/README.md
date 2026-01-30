# End-to-End Cloud Data Pipeline (GCP)

## Overview
This project implements an end-to-end, incremental data pipeline using Google Cloud Platform.
The pipeline ingests NYC Taxi trip data, stores raw data in Cloud Storage, loads it into BigQuery,
and transforms it into analytics-ready tables using dbt.

## Architecture

![Architecture](architecture.png)


## Tech Stack
- Python
- Google Cloud Storage
- BigQuery
- dbt
- SQL

## Key Features
- Incremental ingestion using timestamp-based state tracking
- Idempotent pipeline (safe re-runs)
- Schema-controlled ingestion
- Analytics-ready fact tables
- Data quality tests using dbt

## Final Output
- `fact_trips_daily`: Daily aggregated trip metrics
