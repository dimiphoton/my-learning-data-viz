---
marp: true
theme: default
paginate: true
header: "Automated Replenishment System"
footer: "Dimitri MARCHAND"
---

# Automated Replenishment Dashboard
### A Tableau Solution for Monitoring Supply Chain Performance
#### Dimitri Marchand  


# Automated Replenishment System
### Dashboard Design for a Supply Chain Expert



<!-- 
Welcome to this presentation on the **Automated Replenishment System**.  
We will walk through the dashboard design, data insights, and how this system helps supply chain experts.
-->

---

## Agenda

1. Project Context  
2. Key Objectives  
3. Data Preparation  
4. Data Modeling  
5. Visualizations Overview  
6. Dashboard Design  
7. Challenges Faced  
8. Recommendations & Next Steps  
9. Q&A



<!--  
This is the agenda for our discussion. The goal is to ensure that supply chain experts can effectively monitor the system and take timely action.

---

## Project Context

- **Objective:** Implement a machine learning-based replenishment system for 100 stores in 10 countries.
- **Role:** Senior Data Scientist designing a monitoring dashboard.
- **Goal:** Ensure product availability while minimizing overstock.
- **Challenge:** Balancing stock levels with fluctuating demand.

<!--


The main challenge is ensuring the right balance between stock availability and avoiding overstock. The system should automate replenishment while allowing for manual intervention when needed.
-->
---

## Key Objectives

1. **Monitor Current Performance**  
   - Track stock levels and replenishment success.
2. **Highlight Issues**  
   - Identify low stock, delayed orders, and underperforming stores.
3. **Enable Manual Intervention**  
   - Provide insights for managing exceptions.
4. **Facilitate Data Exploration**  
   - Interactive filtering by store, product, or region.

<!--  
These objectives ensure that supply chain experts can monitor trends, identify risks, and take proactive measures.
-->
---

## Data Preparation

### **Data Sources**
- **Sales Data:** Daily transactions, product categories, revenue.
- **Inventory Data:** Stock levels, thresholds, trends.
- **Replenishment Orders:** Order dates, statuses, delivery timelines.
- **Store Locations:** Country, city, latitude, longitude.

### **Key Columns**
- `StoreID`, `ProductID`, `Category`, `StockLevel`, `ReplenishmentThreshold`
- `OrderDate`, `DeliveryDate`, `OrderStatus`, `SupplierID`
- `Latitude`, `Longitude`


<!--
We used multiple data sources to provide a comprehensive view.  
Key columns include stock levels, order dates, and geospatial information.
-->

---

## Data Modeling

### **Steps Taken:**
1. **Merging Datasets:** Joined sales, inventory, and replenishment data.
2. **Feature Engineering:** Created calculated fields like `DaysToDelivery` and `StockoutRisk`.
3. **Aggregations:** Summarized by store, product category, and time period.
4. **Validation:** Ensured data integrity before dashboard integration.



<!--  
To build a useful dashboard, we combined multiple datasets and engineered key features to help with decision-making.
-->
---

## Visualizations Overview

1. **KPIs (Cards)**  
   - Total Stores, Stockouts, Replenishment Success Rate.
2. **Stock Trends (Bar Chart)**  
   - Compare stock levels vs. thresholds.
3. **Sales Trends (Line Chart)**  
   - Analyze trends over time.
4. **Replenishment Table**  
   - Track order statuses.
5. **Geospatial Analysis (Map)**  
   - Store performance and stockout risks.



<!--  
These visuals ensure a complete overview. KPIs provide quick insights, while charts and tables allow detailed analysis.
-->
---

## Dashboard Design: Tab 1

### **Executive Summary**
- **KPIs:** Total Stores, Stockouts, Replenishment Success Rate.
- **Geospatial Map:** Store performance and stockout risks by country.
- **Stock Levels (Bar Chart):** Highlight products below thresholds.

### **Interactivity**
- Filters for country, product category, and date range.
- Hover tooltips for details.



<!--  
The **Executive Summary** tab gives a high-level overview of key performance indicators. The map helps visualize geographic trends.
-->
---

## Dashboard Design: Tab 2

### **Detailed Analysis**
- **Sales Trends (Line Chart)**  
   - Analyze patterns over time.
- **Replenishment Table**  
   - Monitor pending and delayed orders.
- **Stock Trends**  
   - Historical stock levels by store or category.

### **Interactivity**
- Drilldowns by product, store, or region.
- Sorting and filtering options.



<!--  
The **Detailed Analysis** tab allows deeper investigation. Users can track sales trends and identify supply chain bottlenecks.
-->
---

## Challenges Faced

1. **Data Quality**  
   - Missing or inconsistent values in datasets.
2. **Scalability**  
   - Ensuring the dashboard performs well with large data.
3. **User Interactivity**  
   - Keeping it user-friendly while offering deep insights.



<!--  
We faced challenges with data quality, system performance, and user experience. These were addressed through careful preprocessing and design.
-->
---

## Recommendations & Next Steps

1. **Enhance Predictive Models**  
   - Improve demand forecasts.
2. **Automate Reporting**  
   - Set up scheduled email alerts for critical KPIs.
3. **Expand Scope**  
   - Include supplier performance metrics and cost analyses.
4. **User Training**  
   - Workshops for effective dashboard usage.



<!--  
The next steps involve refining predictive analytics, automating alerts, and expanding the dashboard's capabilities.
-->
---

# Thank You  
### Questions?



<!--  
Thank you for your time! I am happy to take any questions about the dashboard and its design.
-->