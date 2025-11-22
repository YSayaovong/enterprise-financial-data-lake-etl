
# Enterprise Financial Data Lake ETL  
**Data Engineering + Data Analytics Project**

This project is a fully containerized **Financial Data Lake ETL pipeline** designed for real-world data engineering workflows.  

It extracts historical stock data from Yahoo Finance, transforms it into analytics‑ready tables, and loads it into a PostgreSQL data lake.  

A full **Power BI Analytics Dashboard** visualizes KPIs, trends, and investment insights based on the processed data.

---

## 🚀 Project Architecture

The system is built using a modular ETL architecture:

1. **Extract**  
   - Uses Yahoo Finance API via `yfinance`  
   - Pulls 5 years of daily historical data for multiple tickers  
   - Saves raw data into structured Python objects

2. **Transform**  
   - Cleans, standardizes, and validates datasets  
   - Renames fields, enforces schema, ensures proper typing  
   - Maps tickers to instrument IDs

3. **Load**  
   - Persists clean datasets into PostgreSQL  
   - Two key fact/dimension tables:
     - `instruments`
     - `daily_prices`

4. **Analytics Layer**
   - Power BI connects directly to PostgreSQL
   - KPI metrics and trend reports generated with DAX

---

## 🧱 System Diagram

![System Diagram](https://github.com/YSayaovong/enterprise-financial-data-lake-etl/blob/main/assets/ETL-Financial-BI-Dashboard-Summary.png?raw=true)

This diagram represents the full data flow:
- External data source → Python ETL → Postgres Data Lake → Power BI Dashboard

---

## 📊 Database Tables

### **Instruments Table**
Stores master metadata about each tracked financial instrument.

![Instruments Table](https://github.com/YSayaovong/enterprise-financial-data-lake-etl/blob/main/assets/instrument.PNG?raw=true)

---

### **Daily Prices Table**
Stores per‑day OHLCV financial data for each instrument.

![Daily Prices Table](https://github.com/YSayaovong/enterprise-financial-data-lake-etl/blob/main/assets/daily.PNG?raw=true)

---

### **SQL View of Tables**
A snapshot of the PostgreSQL schema and row-level data:

![SQL Table Preview](https://github.com/YSayaovong/enterprise-financial-data-lake-etl/blob/main/assets/sql_table.PNG?raw=true)

---

## 📈 Analytics & Power BI Dashboard

A complete investment analytics dashboard was developed using Power BI.

It features:
- Multi‑year trend analysis  
- Key performance indicators (KPIs)  
- OHLC trends  
- Volume‑based volatility insights  
- Cross‑instrument comparisons  

### **KPI Summary**
![KPI Summary](https://github.com/YSayaovong/enterprise-financial-data-lake-etl/blob/main/assets/kpi_summary.PNG?raw=true)

### **Power BI Dashboard Overview**
![Power BI Dashboard](https://github.com/YSayaovong/enterprise-financial-data-lake-etl/blob/main/assets/power_bi.PNG?raw=true)

---

## 🛠 Tech Stack

**Languages & Tools**  
- Python  
- PostgreSQL  
- Docker & Docker Compose  
- Power BI  
- Pandas  
- SQLAlchemy  
- YFinance  

**Engineering Concepts Used**  
- Modular ETL pipeline design  
- Data normalization  
- Database schema modeling  
- Batch processing  
- Data quality validation  
- Dockerized development environments  
- Business intelligence reporting  

---

## 🧩 How to Run the ETL Pipeline

### 1. Start Docker
```sh
docker compose up --build
```

### 2. Connect to Postgres
```sh
docker exec -it enterprise-financial-data-lake-etl-db-1 psql -U finance -d finance_lake
```

### 3. Run ETL Pipeline
The pipeline runs automatically on container startup, fetching:
```
AAPL, MSFT, GOOG, AMZN, META, TSLA
```

### 4. Refresh Power BI Dashboard  
Connect Power BI to:
```
Host: localhost
Port: 5432
Database: finance_lake
User: finance
Password: finance
```

---

## 📥 Data Sources
- **Yahoo Finance API**  
Used for historical OHLCV data.

---

## ⭐ Why This Project Matters

This project replicates the exact workflow used in modern data teams—ingestion, transformation, storage, and BI reporting—demonstrating readiness for Data Engineering, Analytics Engineering, or Data Analyst roles.

It shows real-world capabilities:

✔ Designing maintainable ETL pipelines
✔ Building normalized relational models for analytics
✔ Automating ingestion of high-volume external data
✔ Using Docker for production-style workflows
✔ Developing end-to-end dashboards for business stakeholders

This project proves the ability to turn raw financial data into decision-ready insights, exactly what companies expect from a modern data engineer or analyst.

---

## 📌 Future Enhancements
- Add pipeline scheduling using Airflow  
- Expand instruments to crypto, ETFs, and forex  
- Add anomaly detection models  
- Implement slowly changing dimensions (SCD)  
- Deploy dashboard to Power BI Service

---

## 📬 Contact  
If you want this packaged for portfolio presentation or recruiter optimization, just ask—easy upgrade.

