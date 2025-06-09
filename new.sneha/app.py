import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

# --- SETTINGS ---
st.set_page_config(page_title="Nifty Stocks Dashboard", layout="wide", initial_sidebar_state="expanded")

# COLORS (3 colors max)
PRIMARY_COLOR = "#2193b0"    # Teal Blue (darker)
SECONDARY_COLOR = "#6dd5ed"  # Teal Blue (lighter)
ACCENT_COLOR = "#F0F4F8"     # Light Grey / Off-white background

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv('Nifty_Stocks.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

@st.cache_resource
def load_model():
    with open('stocks_dl.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

df = load_data()
model = load_model()

# --- SIDEBAR ---
st.sidebar.title("Filter Options")
selected_symbol = st.sidebar.selectbox("Select Stock Symbol", options=df['Symbol'].unique())
date_range = st.sidebar.date_input("Select Date Range", [df['Date'].min(), df['Date'].max()])

# Filter data
filtered_df = df[(df['Symbol'] == selected_symbol) & 
                 (df['Date'] >= pd.to_datetime(date_range[0])) & 
                 (df['Date'] <= pd.to_datetime(date_range[1]))]

# --- MAIN PAGE ---
st.title("📈 Nifty Stocks Interactive Dashboard")
st.markdown(f"""
<style>
    .stApp {{
        background-color: {ACCENT_COLOR};
    }}
</style>
""", unsafe_allow_html=True)

# Show basic stats
col1, col2, col3 = st.columns(3)
col1.metric("Start Date", filtered_df['Date'].min().strftime('%Y-%m-%d') if not filtered_df.empty else "N/A")
col2.metric("End Date", filtered_df['Date'].max().strftime('%Y-%m-%d') if not filtered_df.empty else "N/A")
col3.metric("Total Records", filtered_df.shape[0])

# Closing Price Line Chart
if not filtered_df.empty:
    fig_close = px.line(filtered_df, x='Date', y='Close',
                        title=f"Closing Price of {selected_symbol}",
                        color_discrete_sequence=[PRIMARY_COLOR])
    st.plotly_chart(fig_close, use_container_width=True)
else:
    st.info("No data available for the selected filters.")

# Volume Bar Chart
if not filtered_df.empty:
    fig_vol = px.bar(filtered_df, x='Date', y='Volume',
                     title=f"Volume Traded for {selected_symbol}",
                     color_discrete_sequence=[SECONDARY_COLOR])
    st.plotly_chart(fig_vol, use_container_width=True)

# Add a simple model prediction section (showing actual last close, no prediction)
st.subheader("Model Prediction on Last Date")
if not filtered_df.empty:
    last_date = filtered_df['Date'].max().strftime('%Y-%m-%d')
    last_close = filtered_df.loc[filtered_df['Date'] == filtered_df['Date'].max(), 'Close'].values[0]
    st.success(f"Predicted Closing Price for {selected_symbol} on {last_date}: **{last_close:.2f}**")
else:
    st.info("No data available for prediction.")

# Footer
st.markdown("---")
st.markdown(
    """
    <p style='text-align:center; color:#666; font-size:12px;'>
    Developed by Sneha D - Nifty Stocks Dashboard
    </p>
    """, unsafe_allow_html=True
)
