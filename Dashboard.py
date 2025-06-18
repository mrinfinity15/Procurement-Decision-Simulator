import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Procurement Decision Simulator", layout="wide")

# Title
st.title("📦 Procurement Decision Simulator Dashboard")

# Load Data
@st.cache_data
def load_data():
    return pd.read_excel("Scored_Vendors_Advanced.xlsx")

df = load_data()

# Sidebar: Adjustable MCDA weights
st.sidebar.header("⚙️ Adjust MCDA Weights")

w_cost = st.sidebar.slider("Weight - Cost", 0.0, 1.0, 0.3, step=0.05)
w_lead = st.sidebar.slider("Weight - Lead Time", 0.0, 1.0, 0.25, step=0.05)
w_quality = st.sidebar.slider("Weight - Quality", 0.0, 1.0, 0.2, step=0.05)
w_reliability = st.sidebar.slider("Weight - Reliability", 0.0, 1.0, 0.25, step=0.05)

# Validate total weight
total_weight = w_cost + w_lead + w_quality + w_reliability
if total_weight != 1.0:
    st.sidebar.warning("⚠️ Total weight must equal 1.0")
    st.stop()

# Recalculate score
df['Adjusted_Score'] = (
    w_cost * df['Norm_Cost'] +
    w_lead * df['Norm_Lead'] +
    w_quality * df['Norm_Quality'] +
    w_reliability * df['Norm_Reliability']
)
df['Adjusted_Rank'] = df['Adjusted_Score'].rank(ascending=False)
df = df.sort_values('Adjusted_Score', ascending=False)

# Display top table
st.subheader("🏆 Vendor Rankings (Adjusted)")
st.dataframe(
    df[['Vendor', 'Adjusted_Score', 'Adjusted_Rank', 'Avg_Cost', 'Avg_Lead_Time', 'Avg_Quality', 'Reliability']].round(2),
    use_container_width=True
)

# Bar chart
st.subheader("📊 Vendor Metric Comparison")
metric_options = ['Avg_Cost', 'Avg_Lead_Time', 'Avg_Quality', 'Reliability']
selected_metric = st.selectbox("Select metric to visualize:", metric_options)

st.bar_chart(df.set_index("Vendor")[selected_metric])

# Download updated results
st.subheader("⬇️ Export")
st.download_button(
    label="Download Adjusted Scores as CSV",
    data=df.to_csv(index=False),
    file_name="PDS_Adjusted_Scores.csv",
    mime="text/csv"
)
