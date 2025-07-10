# main.py

from eda import load_data, preprocess, analyze

def main():
    print("Welcome to TrendPy! 📊")
    csv_path = input("Enter path to your UPI dataset CSV file: ").strip('"')

    try:
        df = load_data(csv_path)
        print(f"📄 Columns in dataset: {df.columns.tolist()}")

        df = preprocess(df)
        analyze(df)
        from report_generator import create_pdf_report

        image_paths = {
            "1. App Usage Frequency": "reports/visuals/app_usage_frequency.png",
            "2. Monthly Transaction Value": "reports/visuals/monthly_transaction_value.png",
            "3. Top 5 Apps Pie": "reports/visuals/top_5_apps_pie.png",
            "4. Transaction Trend": "reports/visuals/transaction_value_trend.png",
            "5. Feature Importance": "reports/visuals/feature_importance.png",
            "6. Forecast Transaction Trend": "reports/visuals/forecast_trend.png"
        }

        create_pdf_report(image_paths)
        print("📝 PDF Report saved to 'reports/Digital_Payments_Report.pdf'")

        print("✅ Analysis complete! Check 'reports/visuals/' for charts.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

