# 🏦 Case Study: Eliminating Manual Financial Reporting With a Scalable Data Lake Pipeline  
**Enterprise ETL System for Automated Financial Analytics & KPI Standardization**

## ✅ Executive Summary  
The finance organization of a mid-sized company struggled with slow, inconsistent reporting.  
Analysts spent **4–6 hours every month** manually pulling CSVs, merging spreadsheets, and recalculating KPIs—leading to:

- Conflicting revenue totals across business units  
- Delayed month-end close  
- No single source of truth for financial KPIs  
- Limited drill-down capability without rebuilding spreadsheets  

To solve this, a fully automated **Financial Data Lake + ETL Pipeline** was engineered, replacing all manual steps and enabling real-time, repeatable analytics.

---

# ✅ Step 1 — Financial Data Ingestion Into the Data Lake (Raw Zone)

All incoming financial data—GL extracts, transactions, expense logs, forecast submission files—are automatically routed into the **S3 raw zone**.

### ✅ ETL Enhancements  
- Enforced standardized file naming conventions  
- Automated ingestion scripts replaced manual file drops  
- Metadata tagging for traceability and audit readiness  
- Timestamped storage ensures historical integrity  

### 📊 Pipeline Summary View  
![Financial BI Dashboard Summary](https://github.com/YSayaovong/financial-data-engineering-etl-pipeline/blob/main/Screenshots/ETL-Financial-BI-Dashboard-Summary.png)

This ensures consistent, traceable ingestion for all financial datasets required for reporting and forecasting.

---

# ✅ Step 2 — Transformation Layer Using Apache Spark

Spark processes the raw files and transforms them into fully curated financial datasets.

### ✅ Transformation Logic  
- Schema alignment across months and departments  
- Cleansing invalid/empty records  
- Hierarchical joins (Revenue ↔ Cost ↔ Product ↔ GL ↔ Cost Center)  
- Time-series rollups: **MoM, YoY, QTD, YTD**  
- Deduplication and strict data type enforcement  

### 📈 ETL KPI Flow  
![ETL KPI Flow](https://github.com/YSayaovong/financial-data-engineering-etl-pipeline/blob/main/Screenshots/financial_etl_kpi.PNG)

These curated tables populate the **analytics zone**, ready for consumption by downstream BI tools.

---

# ✅ Step 3 — KPI Modeling & Automated Data Quality Enforcement  

After transformation, the pipeline computes standardized financial KPIs used across FP&A and Accounting:

### ✅ Standard Financial Metrics  
- Revenue  
- COGS  
- Gross Margin  
- Operating Expenses (OPEX)  
- Net Income  
- Forecast vs Actual Variance  
- Rolling 12-Month Trends  

### ✅ Data Quality Monitoring  
The pipeline automatically flags:

- Negative or inconsistent revenue  
- Invalid GL accounts  
- Missing cost center mappings  
- Forecast misalignments  
- Duplicate month entries  

### 📊 KPI Summary Model  
![KPI Summary](https://github.com/YSayaovong/financial-data-engineering-etl-pipeline/blob/main/Screenshots/kpi_summary.PNG)

Finance teams no longer waste time reconciling mismatched spreadsheets.

---

# ✅ Step 4 — BI Delivery Through Power BI  

Curated datasets feed into a Power BI financial model that provides:

### ✅ Executive-Level Reporting  
- Revenue & expense trendlines  
- Gross margin KPIs  
- Forecast vs actual analysis  
- Department-level drill-downs  
- Month-to-date & quarter-to-date performance  
- Automated variance visuals  

The dashboard refreshes daily, giving leadership near real-time visibility.

### 📊 Power BI Dashboard Output  
![Power BI Dashboard](https://github.com/YSayaovong/financial-data-engineering-etl-pipeline/blob/main/Screenshots/power_bi.PNG)

---

# ✅ Step 5 — Business Impact  

After one quarter of adopting the automated financial pipeline:

- ✅ Manual reporting time decreased **by 80%**  
- ✅ KPIs became standardized across Accounting, Finance, and FP&A  
- ✅ Month-end close accelerated  
- ✅ CFO gained same-day insight into financial performance  
- ✅ Analysts focused on strategy instead of spreadsheet processing  
- ✅ Data lake became the backbone for reporting, forecasting, and audit support  

This ETL pipeline now serves as the company’s **financial analytics operating system**, enabling reliable, consistent, and scalable financial reporting.

---

# ✅ Tools & Technologies  
- AWS S3 (Data Lake Raw & Analytics Zones)  
- Apache Spark (ETL Transformation)  
- Python (Data Processing Logic)  
- Power BI (Executive Dashboards)  
- Financial Modeling (Variance, Margin, Trend Analysis)  
- Git/GitHub for version control  

---

# ✅ Summary  
This project demonstrates how an engineered data lake pipeline can modernize financial reporting by automating ingestion, enforcing data integrity, and delivering real-time dashboards.  
The result is a scalable architecture that replaces error-prone spreadsheets with a controlled, enterprise-grade financial analytics environment.

