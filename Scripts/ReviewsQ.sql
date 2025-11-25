SELECT 
	   [ReviewID]
      ,[CustomerID]
      ,[ProductID]
      ,[ReviewDate]
      ,[Rating]
      ,REPLACE([ReviewText],'  ',' ') as ReviewText -- Clean the reviewtext columns by removing the extra spaces
  FROM [PortfolioProject_MarketingAnalytics].[dbo].[customer_reviews]
