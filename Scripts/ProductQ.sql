SELECT [ProductID]
      ,[ProductName]
      ,[Price],

	  CASE

		WHEN [Price] < 50 THEN 'Low'
		WHEN [Price] Between 50 And 200 THEN 'Medium'
		ELSE 'High'

	  END AS PriceCategory

  FROM [PortfolioProject_MarketingAnalytics].[dbo].[products]
