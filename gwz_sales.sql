 SELECT
   date_date
   ,SUM(turnover) AS turnover
 FROM gwz_sales
 GROUP BY date_date
