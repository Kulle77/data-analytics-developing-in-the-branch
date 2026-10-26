 SELECT
   date_date
   ,SUM(turnover) AS turnover
   ,SUM(purchase_cost)
 FROM gwz_sales
 GROUP BY date_date
