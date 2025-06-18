import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("US_Regional_Sales_Data.csv")

# Clean and convert necessary columns
df['Unit Cost'] = df['Unit Cost'].replace(r'[\$,]', '', regex=True).astype(float)
df['ShipDate'] = pd.to_datetime(df['ShipDate'], format="%d/%m/%Y", errors='coerce')
df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'], format="%d/%m/%Y", errors='coerce')

# Calculate lead time in days
df['Lead_Time'] = (df['DeliveryDate'] - df['ShipDate']).dt.days

# Simulate promised delivery date (assumed: ShipDate + 7 days)
df['PromisedDate'] = df['ShipDate'] + pd.Timedelta(days=7)

# Delivery reliability: whether DeliveryDate was on or before PromisedDate
df['OnTime'] = (df['DeliveryDate'] <= df['PromisedDate']).astype(int)

# Simulate quality score (between 80 and 100)
np.random.seed(42)
df['Quality'] = np.random.randint(80, 101, size=len(df))

# Rename for clarity
df = df.rename(columns={
    'WarehouseCode': 'Vendor',
    'Unit Cost': 'Cost'
})

# Filter and drop missing values
df = df[['Vendor', 'Cost', 'Lead_Time', 'Quality', 'OnTime', 'ShipDate']].dropna()

# Group by vendor and calculate averages
vendor_summary = df.groupby('Vendor').agg({
    'Cost': 'mean',
    'Lead_Time': 'mean',
    'Quality': 'mean',
    'OnTime': 'mean'  # this is reliability
}).reset_index()

# Rename columns for clarity
vendor_summary = vendor_summary.rename(columns={
    'Cost': 'Avg_Cost',
    'Lead_Time': 'Avg_Lead_Time',
    'Quality': 'Avg_Quality',
    'OnTime': 'Reliability'
})

# Normalize metrics (higher = better)
vendor_summary['Norm_Cost'] = 1 - ((vendor_summary['Avg_Cost'] - vendor_summary['Avg_Cost'].min()) /
                                   (vendor_summary['Avg_Cost'].max() - vendor_summary['Avg_Cost'].min()))
vendor_summary['Norm_Lead'] = 1 - ((vendor_summary['Avg_Lead_Time'] - vendor_summary['Avg_Lead_Time'].min()) /
                                   (vendor_summary['Avg_Lead_Time'].max() - vendor_summary['Avg_Lead_Time'].min()))
vendor_summary['Norm_Quality'] = ((vendor_summary['Avg_Quality'] - vendor_summary['Avg_Quality'].min()) /
                                  (vendor_summary['Avg_Quality'].max() - vendor_summary['Avg_Quality'].min()))
vendor_summary['Norm_Reliability'] = ((vendor_summary['Reliability'] - vendor_summary['Reliability'].min()) /
                                      (vendor_summary['Reliability'].max() - vendor_summary['Reliability'].min()))

# Define weights for scoring (adjustable)
W_cost = 0.3
W_lead = 0.25
W_quality = 0.2
W_reliability = 0.25

# Calculate final MCDA score
vendor_summary['Final_Score'] = (
    W_cost * vendor_summary['Norm_Cost'] +
    W_lead * vendor_summary['Norm_Lead'] +
    W_quality * vendor_summary['Norm_Quality'] +
    W_reliability * vendor_summary['Norm_Reliability']
)

# Rank vendors
vendor_summary['Rank'] = vendor_summary['Final_Score'].rank(ascending=False)
vendor_summary = vendor_summary.sort_values('Final_Score', ascending=False)

# Save result to Excel
vendor_summary.to_excel("Scored_Vendors_Advanced.xlsx", index=False)

print("✅ Scored vendors saved to Scored_Vendors_Advanced.xlsx")
