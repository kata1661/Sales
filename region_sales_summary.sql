-- Filename: region_sales_summary.sql
-- Author: Katarzyna
-- Description: This query calculates the total sales for each region
--              and groups the results.

SELECT
    region,
    SUM(sales) AS total_sales
FROM
    public.sales_data
GROUP BY
    region;