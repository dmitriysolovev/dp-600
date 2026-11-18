CREATE TABLE [dbo].[product] (
    [ProductKey]      INT              NULL,
    [ProductCode]     VARCHAR (8000)   NULL,
    [ProductName]     VARCHAR (8000)   NULL,
    [Manufacturer]    VARCHAR (8000)   NULL,
    [Brand]           VARCHAR (8000)   NULL,
    [Color]           VARCHAR (8000)   NULL,
    [WeightUnit]      VARCHAR (8000)   NULL,
    [Weight]          VARCHAR (8000)   NULL,
    [Cost]            NUMERIC (38, 18) NULL,
    [Price]           NUMERIC (38, 18) NULL,
    [CategoryKey]     INT              NULL,
    [CategoryName]    VARCHAR (8000)   NULL,
    [SubCategoryKey]  INT              NULL,
    [SubCategoryName] VARCHAR (8000)   NULL
);


GO