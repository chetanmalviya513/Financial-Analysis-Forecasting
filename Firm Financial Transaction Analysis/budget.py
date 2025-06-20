import pandas as pd
import numpy as np
from datetime import datetime

# Function to read and preprocess transaction data
def load_transaction_data(file_path):
    """Load transaction data from a CSV file and preprocess it."""
    data = pd.read_csv(C:\Users\abc\Desktop\Chetan PNB AC\Passbook_2018_2024)
    data['Date'] = pd.to_datetime(data['Date'])
    data['Amount'] = data['Amount'].astype(float)
    return data

# Function to categorize transactions
def categorize_transactions(data):
    """Categorize transactions into Income, Expense, and Savings."""
    data['Category'] = np.where(data['Amount'] > 0, 'Income', 'Expense')
    return data

# Function to generate a monthly summary
def monthly_summary(data):
    """Summarize income and expenses by month."""
    data['Month'] = data['Date'].dt.to_period('M')
    summary = data.groupby(['Month', 'Category'])['Amount'].sum().unstack(fill_value=0)
    summary['Net Savings'] = summary.get('Income', 0) + summary.get('Expense', 0)
    return summary

# Function to forecast future budget
def forecast_budget(summary, months=6):
    """Forecast future budget based on historical averages."""
    avg_income = summary['Income'].mean() if 'Income' in summary else 0
    avg_expense = summary['Expense'].mean() if 'Expense' in summary else 0
    avg_savings = summary['Net Savings'].mean()

    forecast = {
        'Month': pd.date_range(start=datetime.today(), periods=months, freq='M').strftime('%Y-%m'),
        'Forecasted Income': [avg_income] * months,
        'Forecasted Expense': [avg_expense] * months,
        'Forecasted Savings': [avg_savings] * months
    }
    return pd.DataFrame(forecast)

# Function to export data to a file
def export_to_csv(data, file_name):
    """Export a DataFrame to a CSV file."""
    data.to_csv(file_name, index=False)

# Example workflow
def main():
    # Load transaction data
    file_path = 'transaction_data.csv'  # Update with your file path
    transaction_data = load_transaction_data(file_path)

    # Categorize transactions
    transaction_data = categorize_transactions(transaction_data)

    # Generate monthly summary
    summary = monthly_summary(transaction_data)
    print("Monthly Summary:")
    print(summary)

    # Forecast future budget
    forecast = forecast_budget(summary)
    print("\nFuture Budget Forecast:")
    print(forecast)

    # Export results
    export_to_csv(forecast, 'future_budget_forecast.csv')
    print("\nForecast exported to 'future_budget_forecast.csv'")

if __name__ == "__main__":
    main()
