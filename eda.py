# eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import warnings

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

def preprocess(df):
    # ✅ Map Period (numeric month) to month names
    month_map = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    df['Month'] = df['Period'].map(month_map)

    # Drop Year column if it exists
    if 'Yr' in df.columns:
        df = df.drop(['Yr'], axis=1)

    return df

def analyze(df, output_dir='reports/visuals'):
    os.makedirs(output_dir, exist_ok=True)

    plt.rcParams.update({'font.size': 12})  # Adjust value as needed (12–14 is usually optimal)

    # ✅ Bar Chart - App Usage Frequency (Improved readability)
    plt.figure(figsize=(18, 8))  # Increased figure size
    app_counts = df['PaymentApps'].value_counts()

    app_counts.plot(kind='bar', color='#56AB91')
    plt.title('Payment App Usage Frequency')
    plt.xlabel('Payment Apps')
    plt.ylabel('Count')

    # 🧹 Clean and adjust x-axis labels
    plt.xticks(
        ticks=range(len(app_counts)),
        labels=app_counts.index,
        rotation=60,  # Tilt more
        ha='right',  # Align right
        fontsize=8  # Slightly smaller font
    )

    plt.tight_layout()
    plt.savefig(f"{output_dir}/app_usage_frequency.png")
    plt.close()

    # ✅ Monthly Transaction Value (Total)
    month_wise = df.groupby('Month')[['TotalTxValue (Cr)']].sum().sort_values('TotalTxValue (Cr)', ascending=False)
    plt.figure(figsize=(18,8))
    sns.barplot(x=month_wise.index, y=month_wise['TotalTxValue (Cr)'], color='#78c6a3')
    plt.title('Monthly Transaction Value (Total)')
    plt.xlabel('Month')
    plt.ylabel('Total Transaction Value (Cr)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/monthly_transaction_value.png")
    plt.close()

    # ✅ Pie Chart - Top 5 Apps by Total Value
    top_apps = df.groupby('PaymentApps')[['TotalTxValue (Cr)']].sum().sort_values('TotalTxValue (Cr)', ascending=False).head(5)
    plt.figure(figsize=(6,4.5))
    # plt.pie(top_apps['TotalTxValue (Cr)'], labels=top_apps.index, autopct='%.1f%%', colors=sns.color_palette('pastel'))
    teal_shades = ['#469d89', '#56ab91', '#67b99a', '#78c6a3', '#88d4ab']
    plt.pie(top_apps['TotalTxValue (Cr)'], labels=top_apps.index, autopct='%.1f%%', colors=teal_shades)

    plt.title('Top 5 Payment Apps by Transaction Value')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top_5_apps_pie.png")
    plt.close()

    # 🔥 New Visual - Transaction Trend Over Time
    transaction_trend_over_time(df, output_dir)
    feature_importance(df, output_dir)  # <--- this was missing
    forecast_transaction_trend(df, output_dir)

def transaction_trend_over_time(df, output_dir):
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

    trend = df.groupby('Month', observed=False)['TotalTxValue (Cr)'].sum().reset_index()

    plt.figure(figsize=(12,6))
    sns.lineplot(x='Month', y='TotalTxValue (Cr)', data=trend, marker='o', color='#036666', sort=False)
    plt.title("Transaction Value Trend Throughout the Year")
    plt.xlabel('Month')
    plt.ylabel('Total Transaction Value (Cr)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/transaction_value_trend.png")
    plt.close()


def feature_importance(df, output_dir='reports/visuals'):
    df_copy = df.copy()

    # Encode categorical variables
    if 'PaymentApps' in df_copy.columns:
        df_copy['PaymentApps'] = LabelEncoder().fit_transform(df_copy['PaymentApps'])

    X = df_copy[['CustomerTxCount (Mn)', 'CustomerTxValue (Cr)', 'TotalTxCount (Mn)', 'PaymentApps']]
    y = df_copy['TotalTxValue (Cr)']

    model = LinearRegression()
    model.fit(X, y)

    importances = pd.Series(model.coef_, index=X.columns).sort_values(ascending=True)

    # Plotting
    plt.figure(figsize=(8,5))
    importances.plot(kind='barh', color='#469d89')
    plt.title("Feature Importance: What drives Total Transaction Value?")
    plt.xlabel("Coefficient Strength")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/feature_importance.png")
    plt.close()



def forecast_transaction_trend(df, output_dir):
    warnings.filterwarnings("ignore")  # suppress convergence warnings

    # Prepare monthly time series
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
    ts = df.groupby('Month', observed=False)['TotalTxValue (Cr)'].sum()
    ts = ts.sort_index()

    # Fit ARIMA (order can be optimized later)
    model = ARIMA(ts, order=(1, 1, 1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=3)  # Predict next 3 months

    # Plot actual + forecast
    plt.figure(figsize=(10, 6))
    ts.plot(label='Actual', marker='o', color='#036666')
    forecast.plot(label='Forecast', linestyle='--', marker='o', color='#56ab91')
    plt.title("ARIMA Forecast: Next 3 Months Transaction Value")
    plt.xlabel("Month")
    plt.ylabel("Total Transaction Value (Cr)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/forecast_trend.png")
    plt.close()

