# 📊 Social Media Impact on Teen Health - ETL Pipeline

This project is a simple **ETL (Extract, Transform, Load) data pipeline** that analyzes the impact of social media usage on teenage mental and physical health.

---

##  Project Overview

The goal of this project is to process and analyze a dataset related to teenage behavior, including:
- Social media usage
- Sleep patterns
- Academic performance
- Stress, anxiety, and depression levels

The pipeline demonstrates how raw data is transformed into analytics-ready data using Python.

---

## Pipeline Architecture

The project follows a basic ETL structure:

### 1. Extract
- Load raw dataset from CSV file

### 2. Transform
- Clean column names
- Handle data types
- Create new features:
  - Screen time to sleep ratio
  - Sleep categories
  - Risk score for mental health
- Encode categorical variables

### 3. Load
- Save cleaned dataset as Parquet file for analytics.

---
### Database
- Added database integration(PostgreSQL)

