import pandas as pd
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Add Year and Month
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Calculate Profit Margin (avoid division by zero)
df['Profit Margin'] = df.apply(
    lambda row: row['Profit'] / row['Sales'] if row['Sales'] != 0 else 0,
    axis=1
)

# Keep only relevant columns
columns_to_keep = [
    'Order Date', 'Year', 'Month', 'Region', 'Category', 'Sub-Category',
    'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit', 'Profit Margin',
    'Customer Name', 'Segment'
]
cleaned_df = df[columns_to_keep]

# Save the cleaned dataset
cleaned_df.to_csv("sample_superstore.csv", index=False)