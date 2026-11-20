
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, trim

# 1. Create Spark Session
spark = SparkSession.builder \
    .appName("IMDb Movie Reviews Analysis") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# 2. Load the Dataset
df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("multiLine", True) \
    .option("escape", '"') \
    .csv("data/IMDB Dataset.csv")

print("\n===== ORIGINAL DATASET SCHEMA =====")
df.printSchema()

print("\n===== FIRST 5 ROWS =====")
df.show(5, truncate=False)

# 3. Clean the Data
cleaned_df = df.filter(
    col("review").isNotNull() &
    col("sentiment").isNotNull() &
    (trim(col("review")) != "") &
    (trim(col("sentiment")) != "")
)

print("\n===== CLEANED DATA =====")
cleaned_df.show(5, truncate=False)

# 4. Analyze the Data
total_reviews = cleaned_df.count()

print("\n===== TOTAL NUMBER OF REVIEWS =====")
print(total_reviews)

print("\n===== SENTIMENT COUNTS =====")
cleaned_df.groupBy("sentiment").count().show()

# 5. Transform the Data
transformed_df = cleaned_df.withColumn(
    "review_length",
    length(col("review"))
)

print("\n===== REVIEWS WITH REVIEW LENGTH =====")
transformed_df.show(5, truncate=False)

# 6. Filter Reviews Longer Than 500 Characters
long_reviews = transformed_df.filter(
    col("review_length") > 500
)

print("\n===== REVIEWS LONGER THAN 500 CHARACTERS =====")
long_reviews.show(10, truncate=False)

print("\n===== COUNT OF REVIEWS LONGER THAN 500 CHARACTERS =====")
print(long_reviews.count())

# 7. Save the Cleaned and Transformed Dataset
transformed_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/cleaned_movie_reviews")

print("\nCleaned and transformed dataset saved successfully!")

# 8. Stop Spark Session
spark.stop()