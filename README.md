# stock-market-time-series-forecasting
**Stock Market Time Series Forecasting Report**

This report presents an in-depth analysis of historical stock market data using time series forecasting techniques. The goal is to model and predict future stock prices based on past performance, enabling better investment decisions and risk management. The analysis focuses on exploratory data analysis, feature engineering, and forecasting using machine learning and deep learning models.

**Data Overview**
The dataset includes daily stock market information such as:
* Date
* Open price
* High price
* Low price
* Close price
* Volume
The data was extracted from CSV files and preprocessed using the Pandas library. Initial inspection was conducted using functions such as `df.info()`, `df.head()`, and `df.describe()`.

**Data Preprocessing**
* **Datetime Conversion:** The 'Date' column was converted to datetime format.
* **Sorting:** The dataset was sorted in ascending order by date.
* **Missing Values:** Missing entries were handled using forward fill and backward fill techniques.
* **Indexing:** The date was set as the index for time series modeling.

**Exploratory Data Analysis (EDA)**
* **Trend Visualization:** Line plots were created to visualize price movement over time.
* **Moving Averages:** 20-day, 50-day, and 200-day moving averages were calculated and plotted.
* **Return Calculations:** Daily returns were computed and their distribution visualized.
* **Volume Analysis:** Histograms and line plots were used to examine trading volume trends.

**Feature Engineering**
* **Lag Features:** Past values of closing price were used as features.
* **Rolling Statistics:** Rolling mean and rolling standard deviation added for trend smoothing.
* **Technical Indicators:**
  * RSI (Relative Strength Index)
  * MACD (Moving Average Convergence Divergence)
  * Bollinger Bands
These features help the model understand momentum and volatility in stock prices.

**Time Series Modeling**
* **Train-Test Split:** Data was divided chronologically into training and testing sets.
* **Scaling:** Features were normalized using MinMaxScaler to improve model performance.
**Models Used:**
* **Linear Regression**
* **Random Forest Regressor**
* **XGBoost**
* **ARIMA**
* **SARIMA**
* **Facebook Prophet**
* **LSTM (Long Short-Term Memory)**

**Model Evaluation**
Model performances were evaluated using R2 Score and Root Mean Squared Error (RMSE):

| Model                   | R2 Score      | RMSE      |
| ----------------------- | ------------- | --------- |
| Linear Regression       | 0.999895      | 4.260454  |
| Random Forest Regressor | 0.999795      | 5.036366  |
| XGBoost                 | 0.998526      | 8.244545  |
| ARIMA                   | -0.007089     | 44.242590 |
| SARIMA                  | -0.065309     | 44.868589 |
| Prophet Model           | -16904.975993 | 61.310513 |
| LSTM                    | -37.487755    | 11.940135 |
* **Best Models:** Linear Regression and Random Forest showed outstanding accuracy with very low error rates.
* **Poor Performers:** ARIMA, SARIMA, Prophet, and LSTM struggled on this dataset due to model-data incompatibility or tuning issues.

**Results**
* The tree-based and linear models were highly effective in capturing the price trend.
* Deep learning and statistical models performed poorly without extensive hyperparameter optimization.
* Short-term forecasts using simpler models were more reliable.

**Conclusion**

The project demonstrated that traditional machine learning models (Linear Regression, Random Forest) can outperform complex models when properly tuned and applied to structured datasets. Model interpretability and low RMSE scores make these preferable for this dataset.

**Future Recommendations**
* Optimize hyperparameters for LSTM, ARIMA, and Prophet.
* Use ensemble learning combining the top 3 models.
* Incorporate external indicators (e.g., sentiment analysis, macroeconomic trends).
* Deploy the model with real-time prediction via a Streamlit dashboard.
This report provides a practical foundation for forecasting stock prices and suggests potential improvements for robustness and accuracy.

