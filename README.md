# Trader Performance vs Market Sentiment Analysis

## Live Dashboard

Interactive Streamlit dashboard:

https://trader-sentiment-dashboard1.streamlit.app/

---

## Project Overview

This project analyzes how **market sentiment (Fear vs Greed)** influences trader behavior and performance using trading activity data from the Hyperliquid exchange combined with the Bitcoin Fear & Greed Index.

The goal of the project is to identify patterns between **market sentiment and trader profitability**, and understand how traders change their behavior during different market sentiment regimes.

The project includes:

- Data cleaning and preprocessing
- Feature engineering for trader behavior
- Sentiment-based performance analysis
- Trader segmentation
- Predictive modeling
- Clustering analysis
- Interactive Streamlit dashboard for visualization

---

## Dataset Description

Two datasets were used in this analysis.

### 1. Fear greed index Dataset
This dataset provides daily market sentiment classification.

Columns include:

- `Date`
- `Classification` (Fear / Greed / Extreme Greed / Neutral)

### 2. historical data Dataset

This dataset contains historical trading activity from the Hyperliquid exchange.

Important fields include:

- `account`
- `execution price`
- `size`
- `side`
- `time`
- `closedPnL`
- `symbol`
- `leverage-related attributes`

The dataset allows analysis of trader behavior such as **profitability, trade size, trading frequency, and risk exposure**.

---

## Methodology

The analysis begins with loading both datasets and performing basic data quality checks, including missing values and duplicates.

Trading timestamps were converted into datetime format and aggregated at the **daily level per trader account**. Since the sentiment dataset is recorded daily, both datasets were merged using the date field so that each trader’s activity could be associated with the corresponding market sentiment classification.

Several behavioral and performance metrics were created, including:

- Daily profit and loss (PnL)
- Trade frequency
- Average trade size
- Win rate
- Number of trades per day

Because explicit leverage values were not consistently available, **position size (Size USD)** was used as a proxy for trading exposure.

Trader segmentation was performed based on **activity levels and risk exposure**, and additional analysis was conducted using **Random Forest predictive modeling** and **K-Means clustering** to identify trader behavior patterns.

---

## Key Insights

- Trading activity tends to increase during **Greed sentiment regimes**, suggesting traders are more active when market conditions appear favorable.

- **Risk exposure tends to increase during Fear regimes**, where traders place larger positions, likely attempting to capture volatility-driven opportunities.

- Traders operating with larger position sizes experience **higher PnL volatility**, demonstrating the trade-off between potential returns and risk exposure.

- Clustering analysis identified multiple trader archetypes, including **conservative traders, high-risk traders, and active scalpers**, each exhibiting distinct trading behaviors.

---

## Strategy Recommendations

Based on the analysis, several strategy recommendations can be derived:

- Reduce leverage or position size during **Fear sentiment regimes** due to higher volatility and increased liquidation risk.

- Increase trading activity during **Greed regimes**, where stronger market participation and momentum may provide more consistent trading opportunities.

- Implement stricter **risk management rules**, including position sizing and stop-loss mechanisms, especially for high-exposure traders.

---

## Output Visualizations


(<img width="419" height="470" alt="image" src="https://github.com/user-attachments/assets/48c6ca47-0add-4b0b-a2d6-f0ec71ab1373" />)

---

### Trade Size vs Profit

![Trade Size vs Profit](images/trade_size_vs_profit.png)

---

### Sentiment vs Profit

![Sentiment vs Profit](images/sentiment_vs_profit.png)

---

### Feature Correlation Heatmap

![Correlation Heatmap](images/correlation_heatmap.png)

---

## Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/trader-sentiment-dashboard.git
cd trader-sentiment-dashboard
pip install -r requirements.txt
streamlit run dashboard.py
