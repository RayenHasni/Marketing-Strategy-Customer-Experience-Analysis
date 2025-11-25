SELECT 
	   [EngagementID]
      ,[ContentID]
      ,UPPER(REPLACE([ContentType], 'Socialmedia', 'Social Media')) as ContentType
      ,[Likes]
      ,FORMAT(CONVERT(DATE, [EngagementDate]), 'dd.MM.yyyy') as EngagementDate
      ,[CampaignID]
      ,[ProductID]
      ,LEFT([ViewsClicksCombined], CHARINDEX('-',[ViewsClicksCombined])-1) as Views
	  ,RIGHT([ViewsClicksCombined], LEN(ViewsClicksCombined) -CHARINDEX('-', [ViewsClicksCombined])) as Clicks
  FROM [PortfolioProject_MarketingAnalytics].[dbo].[engagement_data]

  WHERE ContentType != 'Newsletter'