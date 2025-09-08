import base64

# Your notebook code as a Python string
code = """from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Create Spark session
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [
    ("Alice", 2000),
    ("Bob", 1500),
    ("Charlie", 3000),
    ("Alice", 2200),
    ("Bob", 1800)
]
columns = ["name", "salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show the data
df.show()

# Aggregate: average salary per person
avg_salary_df = df.groupBy("name").agg(avg("salary").alias("avg_salary"))
avg_salary_df.show()

# Collect results
results = avg_salary_df.toPandas().to_dict(orient="records")
summary = f"Average salaries computed for {len(results)} employees: {results}"

# Return summary to API
dbutils.notebook.exit(summary)
"""

# Encode to Base64
encoded = base64.b64encode(code.encode("utf-8")).decode("utf-8")
print(encoded)