import pandas as pd
import psycopg2

# Load CSV
# Using a raw string (r"...") is often safer for Windows paths
df = pd.read_csv(r"C:\Users\katar\OneDrive\Desktop\sample_superstore.csv")

# 🔧 Fix column names
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="Sales Data",
    user="postgres",
    password="Hoplita17!"  # Be careful with passwords in code for real projects!
)
cur = conn.cursor()

# =====================================================================
# ADD THIS SECTION TO CREATE THE TABLE
# =====================================================================
# Use "CREATE TABLE IF NOT EXISTS" so it doesn't fail on subsequent runs
cur.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        id SERIAL PRIMARY KEY,
        order_date DATE,
        year INT,
        month INT,
        region VARCHAR(255),
        category VARCHAR(255),
        sub_category VARCHAR(255),
        product_name TEXT,
        sales NUMERIC(10, 2)
    )
""")
print("✅ Table 'sales_data' is ready.")
# =====================================================================


# Insert each row
# Note: You may need to ensure your CSV's date format is compatible or convert it
# For now, let's assume it works.
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO sales_data (order_date, year, month, region, category, sub_category, product_name, sales)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['order_date'], row['year'], row['month'],
        row['region'], row['category'], row['sub_category'],
        row['product_name'], row['sales']
    ))

# Commit the transaction to make the changes permanent
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("✅ Data imported successfully into PostgreSQL!")