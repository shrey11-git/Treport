# Treport (Trend based Report Generator)
A Python-powered data analysis and PDF report generator for UPI transaction trends in India.

# ※ What Problem Does It Solve?
Startups or small businesses often lack the tools or budget for deep market analytics. Treport bridges that gap by giving you clear, visual insights from UPI transaction data — highlighting usage trends, seasonal spikes, and app-wise dominance. The insights help businesses make smarter decisions, like when to market, where to partner, and how to forecast future demand.

#※ How It Came to Life
Many early-stage companies can’t afford full-blown data teams or paid reports. Treport was built with them in mind.

This tool shows that the majority of transactions happen in the last 3–4 months of the year, driven by festivals, holidays, and sales seasons. Most of these are made through the top 5% of UPI apps.

A smart strategy? Partner with these top apps during peak months and offer your product or service as discount vouchers. It’s a win-win — customers get deals, and your brand reaches new audiences during high-traffic seasons.

#※ Key Features
- CSV Import: Load your own UPI dataset.
- Preprocessing: Cleans and prepares the data.
- Exploratory Analysis:
App usage frequency
Monthly transaction values
Top 5 apps (pie chart)
Feature importance using Linear Regression
Time-based trend line and ARIMA forecast
- PDF Report:
Auto-generates a multi-page PDF with all charts and captions.
- Business Insight:
Ready-to-use charts and trends for pitch decks, investor briefs, or campaign planning.

#※ Tech Stack
- Language: Python 3.9+
- Data Handling: pandas, numpy
- Visualization: matplotlib, seaborn
- ML & Forecasting: scikit-learn, statsmodels (ARIMA)
- Reporting: fpdf

#※ How to Run
-Clone the repo
git clone https://github.com/your-username/treport.git
cd treport
-Install dependencies (recommended in a virtual environment)
pip install -r requirements.txt
-Run the app
python main.py
You’ll be prompted to input the path to your CSV file (e.g., data/upi_2024.csv). The PDF report will be saved under reports/Digital_Payments_Report.pdf.

#※ Charts (Generated using Treport)
- App Usage Frequency (bar chart)
<img width="1800" height="800" alt="app_usage_frequency" src="https://github.com/user-attachments/assets/2152b892-8e99-4871-a0b3-0ab23cbd89ba" />

- Monthly Transaction Value
<img width="1800" height="800" alt="monthly_transaction_value" src="https://github.com/user-attachments/assets/64cdbc2c-b2d0-4693-82e9-eb3f19085edc" />

- Top 5 UPI Apps
<img width="600" height="450" alt="top_5_apps_pie" src="https://github.com/user-attachments/assets/a1f25308-10fa-4f7e-a7a7-c10ddfd822ab" />

- Feature Importance
<img width="800" height="500" alt="feature_importance" src="https://github.com/user-attachments/assets/673a05e9-50a5-4c01-88fb-ea5f5f948c14" />

- Transaction Trend Over Months
<img width="1200" height="600" alt="transaction_value_trend" src="https://github.com/user-attachments/assets/f7c820a6-b8f7-43f2-be7a-e79ee267b69c" />

- Forecast for Next 3 Months
<img width="1000" height="600" alt="forecast_trend" src="https://github.com/user-attachments/assets/c6ff7646-d11f-416a-9134-62bcfba26e63" />


#※ What I Learned
- Real-world data cleaning and preprocessing
- Combining traditional analytics with ML forecasting
- Automating visual storytelling with FPDF
- Packaging insights in a way that’s useful, visual, and actionable for decision-makers

#※ Author
Shreyash Tiwari
[ GitHub](https://github.com/shrey11-git) • [linkedin](http://www.linkedin.com/in/shreyashtiwari-csbs)

TL;DR Summary
Treport helps early-stage companies analyze digital payment trends using Python. It turns raw UPI data into visual insights and a downloadable PDF — perfect for business planning, partnership strategy, and marketing timing.
