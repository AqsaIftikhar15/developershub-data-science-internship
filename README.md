# Part 2 — Data Projects

This folder contains short data projects and demos completed during the internship.

Structure
- `task-1-bank-marketing/` — Bank marketing dataset and analysis notebook (`bank-additional-full.csv`, `notebook.ipynb`).
- `task-2-customer-segmentation/` — K-Means customer segmentation notebook (`notebook.ipynb`). The notebook includes EDA, scaling, elbow method, K-Means, PCA, and cluster interpretation.
- `task-3-streamlit-dashboard/` — Interactive Streamlit dashboard (`app.py`) with `Global_Superstore.csv`, `requirements.txt`, and a README. The app provides sidebar filters, KPIs, top customers, and several visualizations.
- `task-5-streamlit-dashboard/` — Additional Streamlit dashboard files (existing demo).

What was done
- Implemented a complete K-Means segmentation notebook for customer clustering (income vs spending) in `task-2-customer-segmentation`.
- Built an interactive Streamlit app in `task-3-streamlit-dashboard` that loads `Global_Superstore.csv`, provides Region/Category/Sub-Category filters, displays KPIs (sales, profit, order count), top customers, and visualizations (sales by category, profit by region, category share, monthly trend when available). README for the app was also added.
- Small supporting files (requirements) included where relevant.

How to run
- Notebooks: open the notebooks in Jupyter/VS Code and run the cells.
- Streamlit app (task-3):

```bash
cd task-3-streamlit-dashboard
pip install -r requirements.txt
streamlit run app.py
```

Notes & next steps
- Run the Streamlit app locally to validate visuals and interactivity.
- For richer segmentation, add features (age, gender, purchase history) and re-train clusters.
- Consider adding unit tests, exporting filtered reports, and color-coding negative profits in charts.

If you want, I can run the app locally and report the outputs, or add more visualizations and export options.
