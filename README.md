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

### Interactive dashboard - Tableau

Sales change month-to-month or year-to-year.

https://public.tableau.com/views/SalesTrendOverTime_17515601095110/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Sales by Category and Sub-Category

https://public.tableau.com/views/SalesbyCategoryandSub-Category_17515603043920/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Products with high sales but low profit.

https://public.tableau.com/views/ProfitvsSales_17515645341810/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Customer segment with the most sales in each region.

https://public.tableau.com/views/SalesbySegmentandRegion_17515647661800/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link






