CREATE TABLE [dbo].[customer] (
    [CustomerKey]   INT            NULL,
    [GeoAreaKey]    INT            NULL,
    [StartDT]       DATETIME2 (6)  NULL,
    [EndDT]         DATETIME2 (6)  NULL,
    [Continent]     VARCHAR (8000) NULL,
    [Gender]        VARCHAR (8000) NULL,
    [Title]         VARCHAR (8000) NULL,
    [GivenName]     VARCHAR (8000) NULL,
    [MiddleInitial] VARCHAR (8000) NULL,
    [Surname]       VARCHAR (8000) NULL,
    [StreetAddress] VARCHAR (8000) NULL,
    [City]          VARCHAR (8000) NULL,
    [State]         VARCHAR (8000) NULL,
    [StateFull]     VARCHAR (8000) NULL,
    [ZipCode]       VARCHAR (8000) NULL,
    [Country]       VARCHAR (8000) NULL,
    [CountryFull]   VARCHAR (8000) NULL,
    [Birthday]      DATETIME2 (6)  NULL,
    [Age]           INT            NULL,
    [Occupation]    VARCHAR (8000) NULL,
    [Company]       VARCHAR (8000) NULL,
    [Vehicle]       VARCHAR (8000) NULL,
    [Latitude]      VARCHAR (8000) NULL,
    [Longitude]     VARCHAR (8000) NULL
);


GO