# Task 5: Streamlit Dashboard

Interactive dashboard built with Streamlit.

## Overview

This project contains a Streamlit-based dashboard for data visualization and analysis.

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
# Global Superstore — Streamlit Dashboard

## Objective

Create an interactive dashboard showing sales, profit, top customers, and filters by Region, Category, and Sub-Category to help drive targeted business insights.

## What this app provides

- Sidebar filters: **Region**, **Category**, **Sub-Category**
- KPIs: **Total Sales**, **Total Profit**, **Number of Orders**
- Top 5 customers by sales (for selected filters)
- Visualizations: Sales by Category, Profit by Region, Category share pie, Monthly sales trend (if `Order Date` exists)

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

If you prefer to install manually:

```bash
pip install pandas numpy matplotlib seaborn streamlit
```

## Dataset

Place `Global_Superstore.csv` in the same folder as `app.py`. The app expects typical Global Superstore columns such as `Order Date`, `Region`, `Category`, `Sub-Category`, `Customer Name`, `Sales`, and `Profit`.

## Run

Start the app with:

```bash
streamlit run app.py
```

The sidebar filters update KPIs and charts interactively.

## Notes & Insights

- Verify `Order Date` formatting to enable monthly trends.
- Negative profits are displayed as-is; consider color-coding negative bars for clarity.
- Use the `Show raw data` checkbox to inspect the loaded rows.

## Files

- `app.py` — Streamlit application (main)
- `Global_Superstore.csv` — Dataset (place in same folder)
- `requirements.txt` — Python dependencies

## Next steps

- Add export (CSV/PDF) of filtered data
- Add color-coding for negative profit and more layouts for mobile
