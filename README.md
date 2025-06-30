Superstore Sales Data Cleaning & Analysis

data analytics project that takes raw sales data from a CSV file and prepares it for SQL-based analysis. The project includes data cleaning, feature engineering, loading into a PostgreSQL database, and running SQL queries to extract insights.

---

### Data Cleaning & Transformation

- Cleans and preprocesses raw sales data using the **Pandas** library
- Standardizes column names and removes unnecessary fields

### 🧠 Feature Engineering

- Adds new columns such as:
  - `Year`
  - `Month`
  - `Profit Margin` (with division-by-zero handling)

### 🔄 ETL to PostgreSQL

- Loads the cleaned dataset into a **PostgreSQL** database
- Uses `psycopg2` to handle database connections and inserts

### 🛠️ Automated Table Creation

- Automatically creates the `sales_data` table if it doesn't already exist
- Includes proper data types and schema constraints

### 📈 SQL Analysis Ready

- Includes a sample SQL script to:
  - Aggregate **total sales by region**
  - Serve as a foundation for further data analysis or dashboarding

---

## 💻 Technology Stack

| Component      | Description          |
| -------------- | -------------------- |
| Language       | Python               |
| Libraries      | `pandas`, `psycopg2` |
| Database       | PostgreSQL           |
| Query Language | SQL                  |
