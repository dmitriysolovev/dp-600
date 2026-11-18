CREATE TABLE [dbo].[date] (
    [Date]              DATETIME2 (6)  NULL,
    [DateKey]           INT            NULL,
    [Year]              INT            NULL,
    [YearQuarter]       VARCHAR (8000) NULL,
    [YearQuarterNumber] INT            NULL,
    [Quarter]           VARCHAR (8000) NULL,
    [YearMonth]         VARCHAR (8000) NULL,
    [YearMonthShort]    VARCHAR (8000) NULL,
    [YearMonthNumber]   INT            NULL,
    [Month]             VARCHAR (8000) NULL,
    [MonthShort]        VARCHAR (8000) NULL,
    [MonthNumber]       SMALLINT       NULL,
    [DayofWeek]         VARCHAR (8000) NULL,
    [DayofWeekShort]    VARCHAR (8000) NULL,
    [DayofWeekNumber]   INT            NULL,
    [WorkingDay]        INT            NULL,
    [WorkingDayNumber]  VARCHAR (8000) NULL
);


GO