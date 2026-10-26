 SELECT
   date_date
   ,ROUND(SUM(turnover)) AS turnover
   ,ROUND(SUM(purchase_cost))
 FROM gwz_sales
 GROUP BY date_date
