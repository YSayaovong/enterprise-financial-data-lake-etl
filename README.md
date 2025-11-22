# Enterprise Financial Data Lake ETL

A Dockerized **financial data ingestion service** that pulls multi-year historical price data from **Yahoo Finance**, normalizes it, and loads it into a **PostgreSQL data lake**.

This project is designed to look and feel like a real-world **data engineering / backend** system: config-driven, containerized, testable, and ready to be wired into dashboards or downstream analytics.

---

## What This Service Does

- Ingests 5 years of daily OHLCV (Open, High, Low, Close, Volume) data  
- Pulls data for multiple tickers from Yahoo Finance  
- Normalizes raw API responses into a clean relational schema  
- Loads data into PostgreSQL via SQLAlchemy  
- Runs as a Docker Compose stack (`db` + `etl` services)  
- Ensures tables are created automatically on startup  
- Idempotent ingestion (no duplicates on re-run)

---

## Tech Stack

- Python 3  
- yfinance  
- pandas  
- SQLAlchemy  
- PostgreSQL 16  
- Pydantic  
- Docker / Docker Compose  

---

## Project Structure

enterprise-financial-data-lake-etl/  
├─ etl/  
│  ├─ core/  
│  ├─ db/  
│  ├─ pipelines/yahoo/  
│  ├─ run_pipeline.py  
│  └─ settings.py  
├─ Dockerfile  
├─ docker-compose.yml  
├─ requirements.txt  
├─ .env  
└─ README.md  

---

## Running the Pipeline

docker compose down  
docker compose up --build  

---

## Querying the Database

docker exec -it enterprise-financial-data-lake-etl-db-1 psql -U finance -d finance_lake

---

## License

MIT or your choice.
