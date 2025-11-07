## 📚 Case Study: Eliminating Manual Financial Reporting With a Scalable Data Lake Pipeline

### ✅ Scenario
A finance department at a mid-sized organization struggles with reporting delays and inconsistent financial metrics.  
Each month, analysts spend **4–6 hours manually pulling CSVs**, merging spreadsheets, and recalculating KPIs.  
Common issues include:

- Conflicting revenue totals across teams  
- Delayed month-end close  
- No single source of truth for KPIs  
- Inability to drill into trends without re-running manual Excel steps  

Leadership wants a **fully automated data pipeline** to deliver reliable financial analytics without repeated spreadsheet work.

---

### ✅ Step 1 — Data Ingestion Into the Data Lake
All incoming financial files (transactions, GL data, expense logs, forecast inputs) are routed into the data lake’s **raw zone (S3)**.

**ETL Improvements:**
- Standard file naming enforced  
- Metadata tagging added for source tracking  
- Automated load scripts replace manual file drops  

**Pipeline Summary View**  
![Financial BI Dashboard Summary](https://github.com/YSayaovong/financial-data-engineering-etl-pipeline/blob/main/Screenshots/ETL-Financial-BI-Dashboard-Summary.png)

This ensures consistent, timestamped ingestion of all finance datasets.

---

### ✅ Step 2 — Transformation Using Apache Spark
The transformation layer cleans and enriches the raw data:

- Schema alignment across monthly files  
- Handling of null/invalid records  
- Joins for revenue, cost, and product hierarchies  
- Time-series rollups (MOM, YOY, QTD, YTD)  
- Deduplication and type enforcement  

**ETL KPI Flow**  
![ETL KPI Flow](https://github.com/YSayaovong/financial-data-engineering-etl-pipeline/blob/main/Screenshots/financial_etl_kpi.PNG)

Spark pushes these curated datasets into the **analytics zone**, ready for BI consumption.

---

### ✅ Step 3 — KPI Modeling & Data Quality Enforcement
The pipeline computes standardized financial metrics:

- Revenue, COGS, Gross Margin  
- Operating Expenses (OPEX)  
- Net Income  
- Variance vs Forecast  
- Rolling 12-month trends  

Data quality checks automatically flag:

- Negative revenue  
- Invalid GL codes  
- Missing cost centers  
- Forecast mismatches  

**KPI Summary Model**  
![KPI Summary](https://github.com/YSayaovong/financial-data-engineering-etl-pipeline/blob/main/Screenshots/kpi_summary.PNG)

Analysts no longer waste time validating spreadsheets or cleaning mismatched files.

---

### ✅ Step 4 — BI Delivery in Power BI
Curated datasets feed a Power BI model delivering:

- Executive financial summary  
- Revenue & expense trends  
- KPI variance visuals  
- Department-level drill-downs  
- Forecast vs Actual comparisons  

The dashboard refreshes automatically on a schedule.

**Power BI Dashboard Output**  
![Power BI Dashboard](https://github.com/YSayaovong/financial-data-engineering-etl-pipeline/blob/main/Screenshots/power_bi.PNG)

Finance leadership receives **daily refreshed metrics** instead of end-of-month delays.

---

### ✅ Step 5 — Outcomes
After one quarter of using the automated pipeline:

- Manual reporting time dropped by **80%**  
- All KPIs became consistent across finance, FP&A, and accounting  
- CFO gained same-day visibility into month-to-date performance  
- Analysts shifted from data cleanup to strategic, forward-looking analysis  
- Month-end close accelerated due to consistent, trustworthy datasets  

The data lake + ETL pipeline now functions as the organization’s **financial analytics backbone**, supporting reporting, forecasting, audits, and executive decision-making.
