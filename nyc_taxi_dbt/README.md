# dbt Models – NYC Taxi Analytics Layer

## Overview
This directory contains the dbt project responsible for transforming raw NYC Taxi trip data
stored in BigQuery into clean, analytics-ready tables.

The dbt layer follows analytics engineering best practices, including staging models,
fact tables, and automated data quality tests.

---

## Data Sources
- **BigQuery Dataset:** nyc_taxi
- **Source Table:** trips_incremental

This table is populated by an upstream Python ingestion pipeline and serves as the raw input
for all dbt transformations.

---

## Model Structure

### Staging Models
**Location:** models/staging/

Purpose:
- Select required columns from raw tables
- Apply consistent naming and typing
- Provide a clean base for downstream models

Models:
- stg_trips  
  - One row per taxi trip  
  - Cleaned and standardized schema  

---

### Mart Models
**Location:** models/marts/

Purpose:
- Create business-level aggregations
- Support analytics and reporting use cases

Models:
- fact_trips_daily  
  - Daily aggregated taxi trip metrics  
  - Total trips  
  - Total fare amount  
  - Average trip distance  

---

## Data Quality Tests
Data quality is enforced using dbt tests.

Implemented tests include:
- not_null checks on key columns
- unique checks on primary dimensions

Tests are defined in schema.yml files alongside the models.

---

## How to Run dbt

From this directory:

dbt run  
dbt test  

---

## Design Principles
- Clear separation between raw, staging, and analytics layers
- SQL-based transformations managed through dbt
- Reproducible and testable data models
- Designed for scheduled orchestration (e.g., Airflow)
