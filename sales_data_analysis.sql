-- Query 1: Calculate Total Sales, Number of Orders, and Average Sale Value

    ROUND(SUM(sales), 2) AS total_sales,
    COUNT(id) AS number_of_orders,
    ROUND(AVG(sales), 2) AS average_sale_value
FROM
    public.sales_data;

-- Query 2: Total Sales by Year
SELECT
    year,
    ROUND(SUM(sales), 2) AS total_sales
FROM
    public.sales_data
GROUP BY
    year
ORDER BY
    year;

-- Query 3: Total Sales by Region
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales
FROM
    public.sales_data
GROUP BY
    region
ORDER BY
    total_sales DESC;

-- Query 4: Total Sales by Category and Sub-Category
SELECT
    category,
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales
FROM
    public.sales_data
GROUP BY
    category,
    sub_category
ORDER BY
    category,
    total_sales DESC;