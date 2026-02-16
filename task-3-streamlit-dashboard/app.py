import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import cm

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

sns.set_style("whitegrid")

st.title("Global Superstore Dashboard")

@st.cache_data
def load_data(path='Global_Superstore.csv'):
	df = pd.read_csv(path, encoding='latin1')
	return df

df = load_data('Global_Superstore.csv')
st.write("Dataset Loaded Successfully")

if st.checkbox("Show raw data (first 5 rows)"):
	st.dataframe(df.head())

# --- Clean Dataset ---
df = df.copy()
df.dropna(inplace=True)
for col in ['Sales', 'Profit']:
	if col in df.columns:
		df[col] = pd.to_numeric(df[col], errors='coerce')

# Sidebar filters
st.sidebar.header("Filters")

regions = df['Region'].unique() if 'Region' in df.columns else []
cats = df['Category'].unique() if 'Category' in df.columns else []
subcats = df['Sub-Category'].unique() if 'Sub-Category' in df.columns else []

region = st.sidebar.multiselect("Select Region", options=regions, default=list(regions))
category = st.sidebar.multiselect("Select Category", options=cats, default=list(cats))
sub_category = st.sidebar.multiselect("Select Sub-Category", options=subcats, default=list(subcats))

# Apply filters
df_filtered = df.copy()
if len(region) > 0 and 'Region' in df.columns:
	df_filtered = df_filtered[df_filtered['Region'].isin(region)]
if len(category) > 0 and 'Category' in df.columns:
	df_filtered = df_filtered[df_filtered['Category'].isin(category)]
if len(sub_category) > 0 and 'Sub-Category' in df.columns:
	df_filtered = df_filtered[df_filtered['Sub-Category'].isin(sub_category)]

# KPIs
st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)

total_sales = df_filtered['Sales'].sum() if 'Sales' in df_filtered.columns else 0
total_profit = df_filtered['Profit'].sum() if 'Profit' in df_filtered.columns else 0
top_customers = pd.Series(dtype=float)
if 'Customer Name' in df_filtered.columns and 'Sales' in df_filtered.columns:
	top_customers = df_filtered.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Number of Orders", f"{len(df_filtered):,}")

st.subheader("Top 5 Customers by Sales")
if not top_customers.empty:
	st.dataframe(top_customers.rename('Sales'))
else:
	st.write("No customer sales data available for the selected filters.")

# Visualizations
st.subheader("Visualizations")

# Sales by Category
if 'Category' in df_filtered.columns and 'Sales' in df_filtered.columns:
	fig1, ax1 = plt.subplots(figsize=(8, 5))
	cat_sales = df_filtered.groupby('Category')['Sales'].sum().reset_index()
	sns.barplot(x='Category', y='Sales', data=cat_sales, ax=ax1, palette='Set2')
	ax1.set_title('Total Sales per Category')
	ax1.set_ylabel('Sales')
	st.pyplot(fig1)
	plt.clf()

# Profit by Region
if 'Region' in df_filtered.columns and 'Profit' in df_filtered.columns:
	fig2, ax2 = plt.subplots(figsize=(8, 5))
	region_profit = df_filtered.groupby('Region')['Profit'].sum().reset_index()
	sns.barplot(x='Region', y='Profit', data=region_profit, ax=ax2, palette='Set1')
	ax2.set_title('Total Profit per Region')
	ax2.set_ylabel('Profit')
	st.pyplot(fig2)
	plt.clf()

# Category share pie
if 'Category' in df_filtered.columns and 'Sales' in df_filtered.columns:
	fig3, ax3 = plt.subplots(figsize=(6, 6))
	sizes = cat_sales.set_index('Category')['Sales']
	ax3.pie(sizes, labels=sizes.index, autopct='%1.1f%%', startangle=140, colors=cm.Set2.colors)
	ax3.set_title('Category Sales Share')
	st.pyplot(fig3)
	plt.clf()

# Monthly sales trend (if Order Date exists)
if 'Order Date' in df_filtered.columns:
	try:
		df_filtered['Order Date'] = pd.to_datetime(df_filtered['Order Date'], errors='coerce')
		monthly = df_filtered.dropna(subset=['Order Date']).set_index('Order Date').resample('M')['Sales'].sum()
		if not monthly.empty:
			fig4, ax4 = plt.subplots(figsize=(10, 4))
			monthly.plot(ax=ax4)
			ax4.set_title('Monthly Sales Trend')
			ax4.set_ylabel('Sales')
			st.pyplot(fig4)
			plt.clf()
	except Exception:
		pass

st.markdown("---")
st.markdown("**Notes:** Filters on the sidebar update the KPIs and charts. Add more charts or formatting as needed.")
