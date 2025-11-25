
WITH dprecord as (
SELECT 
	   [JourneyID]
      ,[CustomerID]
      ,[ProductID]
      ,[VisitDate]
      ,[Stage]
      ,[Action]
      ,[Duration]
	  ,ROW_NUMBER() Over (Partition By CustomerID, ProductID, VisitDate, Stage, Action  
            ORDER BY JourneyID  ) as rn
  FROM [PortfolioProject_MarketingAnalytics].[dbo].[customer_journey])

----------------------------------------------------------------------------------------

SELECT [JourneyID], [CustomerID], [ProductID], [VisitDate], [Stage], [Action],
	coalesce(Duration, avg_duration) as Duration

FROM (

SELECT  [JourneyID], [CustomerID], [ProductID], [VisitDate], Upper([Stage]) as Stage
, [Action], [Duration]
, AVG(Duration) Over (PARTITION BY VisitDate) as avg_duration
,ROW_NUMBER() OVER (
                PARTITION BY CustomerID, ProductID, VisitDate, UPPER(Stage), Action  -- Groups by these columns to identify duplicate records
                ORDER BY JourneyID  -- Orders by JourneyID to keep the first occurrence of each duplicate
            ) AS rn
 
FROM [PortfolioProject_MarketingAnalytics].[dbo].[customer_journey]

) AS subquery

WHERE rn =1