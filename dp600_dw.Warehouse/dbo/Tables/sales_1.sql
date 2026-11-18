CREATE TABLE [dbo].[sales] (
    [OrderKey]     BIGINT          NULL,
    [LineNumber]   INT             NULL,
    [OrderDate]    DATE            NULL,
    [DeliveryDate] DATE            NULL,
    [CustomerKey]  INT             NULL,
    [StoreKey]     INT             NULL,
    [ProductKey]   INT             NULL,
    [Quantity]     INT             NULL,
    [UnitPrice]    DECIMAL (19, 4) NULL,
    [NetPrice]     DECIMAL (19, 4) NULL,
    [UnitCost]     DECIMAL (19, 4) NULL,
    [CurrencyCode] VARCHAR (3)     NULL,
    [ExchangeRate] DECIMAL (19, 6) NULL
);


GO