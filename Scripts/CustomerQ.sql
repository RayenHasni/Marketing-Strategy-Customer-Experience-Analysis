SELECT c.[CustomerID]
      ,c.[CustomerName]
      ,c.[Email]
      ,c.[Gender]
      ,c.[Age]
	  ,g.Country
	  ,g.City

  FROM [PortfolioProject_MarketingAnalytics].[dbo].[customers] as c

  Left Join

  [PortfolioProject_MarketingAnalytics].dbo.geography as g

  ON c.GeographyID = g.GeographyID