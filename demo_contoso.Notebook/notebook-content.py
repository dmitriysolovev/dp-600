# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "19181ba2-4972-4b81-a4fb-72ee8a9dba6d",
# META       "default_lakehouse_name": "dp600_lh",
# META       "default_lakehouse_workspace_id": "8bc2e9e7-e694-48fe-b734-5aecf436a25b",
# META       "known_lakehouses": [
# META         {
# META           "id": "19181ba2-4972-4b81-a4fb-72ee8a9dba6d"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.types import *
from pyspark.sql.functions import *

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

sales_df_1 = spark.read.format("csv").option("header","true").load("Files/10M/sales.csv")
# df now is a Spark DataFrame containing CSV data from "Files/10M/sales.csv".
display(sales_df_1)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").option("inferSchema","true").load("Files/10M/sales.csv")
# df now is a Spark DataFrame containing CSV data from "Files/10M/sales.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

sales_schema = StructType([
    StructField("OrderKey", IntegerType(), True),
    StructField("LineNumber", IntegerType(), True),
    StructField("OrderDate", DateType(), True),
    StructField("DeliveryDate", DateType(), True),
    StructField("CustomerKey", IntegerType(), True),
    StructField("StoreKey", IntegerType(), True),
    StructField("ProductKey", IntegerType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("UnitPrice", DoubleType(), True),
    StructField("NetPrice", DoubleType(), True),
    StructField("UnitCost", DoubleType(), True),
    StructField("CurrencyCode", StringType(), True),
    StructField("ExchangeRate", DoubleType(), True)
])

sales_df = (
    spark.read
        .format("csv")
        .option("header", "true")
        .option("dateFormat", "yyyy-MM-dd")
        .schema(sales_schema)
        .load("Files/10M/sales.csv")
)

display(sales_df)
sales_df.write.format('delta').mode('overwrite').saveAsTable("contoso.sales_df")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

sales_df = sales_df.withColumn("Year", year(col("OrderDate")))
display(sales_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_2020 = sales_df.filter(
    (col("OrderDate") >= "2020-01-01") &
    (col("OrderDate") < "2021-01-01")
)

display(df_2020)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Convert NetPrice to a common/base currency
df_converted = sales_df.withColumn(
    "NetPrice_Base",
    col("NetPrice") * col("ExchangeRate")
)

# Calculate average NetPrice by year and month
df_monthly_avg = (
    df_converted
    .groupBy(
        year(col("OrderDate")).alias("Year"),
        month(col("OrderDate")).alias("Month")
    )
    .agg(
        round(avg("NetPrice_Base"), 2).alias("AvgNetPrice")
    )
    .orderBy("Year", "Month")
)

display(df_monthly_avg)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
