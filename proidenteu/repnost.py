from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("ExampleApp") \
    .getOrCreate()

# Sample DataFrame creation
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Variable holding the temporary view name
temp_name = "my_temp_view"

# Create or replace the temporary view
df.createOrReplaceTempView(f"{temp_name}")

# Now you can use SQL queries to query the temporary view
result_df = spark.sql(f"SELECT * FROM {temp_name}")
result_df.show()
