import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Trader Performance Dashboard",
    layout="wide"
)

sns.set_style("whitegrid")

# Load data
data = pd.read_csv("final_data.csv")

# Title
st.title("Trader Performance vs Market Sentiment Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

sentiment = st.sidebar.selectbox(
    "Select Market Sentiment",
    data['classification'].dropna().unique()
)

min_trade = st.sidebar.slider(
    "Minimum Trade Size (USD)",
    int(data['Size USD'].min()),
    int(data['Size USD'].max()),
    int(data['Size USD'].min())
)

filtered = data[
    (data['classification'] == sentiment) &
    (data['Size USD'] >= min_trade)
]

# KPI Metrics
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Traders", filtered['Account'].nunique())
col2.metric("Average Daily PnL", round(filtered['daily_pnl'].mean(),2))
col3.metric("Average Trade Size", round(filtered['Size USD'].mean(),2))
col4.metric("Total Trades", int(filtered['num_trades'].sum()))

st.divider()

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(filtered)

st.divider()

# Charts Layout
col1, col2 = st.columns(2)

# PnL Distribution
with col1:
    st.subheader("PnL Distribution")

    fig, ax = plt.subplots()

    sns.histplot(
        filtered['daily_pnl'],
        bins=30,
        kde=True,
        ax=ax
    )

    ax.set_xlabel("Daily PnL")

    st.pyplot(fig)

# Trade Size vs Profit
with col2:
    st.subheader("Trade Size vs Profit")

    fig2, ax2 = plt.subplots()

    sns.scatterplot(
        data=filtered,
        x="Size USD",
        y="daily_pnl",
        hue="classification",
        size="num_trades",
        sizes=(20,200),
        ax=ax2
    )

    ax2.set_xlabel("Trade Size (USD)")
    ax2.set_ylabel("Daily Profit")

    st.pyplot(fig2)

st.divider()

# Sentiment Comparison
st.subheader("Sentiment vs Profit")

fig3, ax3 = plt.subplots()

sns.boxplot(
    data=data,
    x="classification",
    y="daily_pnl",
    ax=ax3
)

ax3.set_xlabel("Market Sentiment")
ax3.set_ylabel("Daily PnL")

st.pyplot(fig3)

st.divider()

# Correlation Heatmap
st.subheader("Feature Correlation")

corr = data[['daily_pnl','Size USD','num_trades']].corr()

fig4, ax4 = plt.subplots()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=ax4
)

st.pyplot(fig4)