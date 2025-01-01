---
marp: false
theme: default
paginate: true
footer: "Part Name | Page {page}"
---

# Automated Replenishment Dashboard
### A Tableau Solution for Monitoring Supply Chain Performance
#### Dimitri Marchand  
*2025-01-01*

---

## Introduction
_Part 1: Introduction_
### The Problem
Efficient inventory management across:
- **100 stores** in **10 countries**.
- High demand variability and complex supply chains.

### The Solution
An interactive Tableau dashboard designed to:
- Monitor performance metrics in real-time.
- Highlight issues and anomalies.
- Assist with manual interventions when needed.

---

## Key Performance Indicators (KPIs)

1. **Fill Rate (%)**: Measures demand met from stock.
2. **Stockout Rate (%)**: Percentage of SKUs out of stock.
3. **Excess Inventory (%)**: Monitors overstock levels.
4. **Lead Time Variance**: Tracks delivery consistency.
5. **Manual Interventions Count**: Overrides by users.

### Why These KPIs?
- Cover operational, financial, and logistical aspects.
- Provide actionable insights.

---

## Dashboard Mock-Up

![Mock-up Overview](https://via.placeholder.com/800x450.png)

### Features:
- **Overview Page**: Trends and anomalies in key metrics.
- **Drill-Down**: Country, store, or product-level insights.
- **Alert Indicators**: Color-coded warnings for critical metrics.

---

## Workflow

1. **Monitor**:
   - View KPI trends on the overview page.
   - Spot anomalies using color-coded alerts.
2. **Investigate**:
   - Use filters to focus on specific stores, SKUs, or regions.
3. **Act**:
   - Perform manual adjustments or validate ML suggestions.
4. **Plan**:
   - Leverage forecasting to prevent future issues.

---

## Design Choices

1. **Visualization**:
   - Line charts for trends.
   - Heatmaps to highlight problem areas.
   - Bar charts for comparisons (e.g., fill rates by region).

2. **User Interface**:
   - Clear navigation with tabs for KPIs, trends, and detailed analysis.
   - Interactive filters for dynamic exploration.

3. **Alerts**:
   - Dynamic thresholds based on historical data.
   - Tooltips for clarity.

---

## Challenges and Mitigations

### Potential Issues:
- **Overloaded Interface**: Too many metrics or visuals.
- **Data Latency**: Delayed updates affecting decisions.
- **Misinterpretation**: Users misunderstanding KPIs.

### Design Solutions:
- Categorize metrics and use tabs.
- Ensure real-time data connectivity.
- Add tooltips and metric definitions.

---

## Future Enhancements

1. **API Integration**:
   - Incorporate external data (e.g., weather, events).
2. **AI Recommendations**:
   - Suggest restocking actions based on advanced ML models.
3. **Mobile Compatibility**:
   - Accessible dashboards for on-the-go monitoring.

---

## Conclusion

### Dashboard Benefits:
- Real-time monitoring of critical supply chain metrics.
- Highlights potential issues for quick resolution.
- Supports both automated and manual decision-making.

### Questions?
