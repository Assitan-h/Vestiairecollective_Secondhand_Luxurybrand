from google.cloud import storage
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim, regexp_replace, when

# Initialize Spark session
spark = SparkSession.builder \
    .appName("VestiaireProcessing") \
    .getOrCreate()


input_gcs_path = "gs://My-bucket-name/data/vestiaire.csv"
output_gcs_path = "gs://My-bucket-name/data/processed/vestiaire_cleaned.csv"
# GCS paths

df = spark.read.option("header", "true").csv(input_gcs_path)
# Read CSV data from GCS

df.show(5, truncate=False)
# Show the data to check if it looks correct

df.printSchema()
# Inspect the schema to see column types

df_clean = df.fillna({
    "price_usd": 0.0,
    "seller_price": 0.0,
    "seller_earning": 0.0,
    "buyers_fees": 0.0,
    "product_like_count": 0,
    "sold": False,
    "reserved": False,
    "available": False,
    "in_stock": False,
    "should_be_gone": False,
    "has_cross_border_fees": False,
    "seller_products_sold": 0,
    "seller_num_products_listed": 0,
    "seller_community_rank": 0,
    "seller_num_followers": 0,
    "seller_pass_rate": 0.0,
})
# Handle missing values (fill nulls with defaults)

columns_to_clean = [
    "product_condition", "product_gender_target", "seller_country",
    "product_material", "product_color", "brand_name", "product_category"
]
for column in columns_to_clean:
    df_clean = df_clean.withColumn(column, lower(trim(col(column))))
# Clean columns 
 
df_clean = df_clean.withColumn(
    "product_description",
    regexp_replace(trim(col("product_description")), r"\s+", " ")
)
# Clean product_description column

df_clean = df_clean.withColumn(
    "brand_id", when(col("brand_id").isNull(), "unknown").otherwise(col("brand_id"))
)
df_clean = df_clean.withColumn(
    "brand_name", when(col("brand_name").isNull(), "unknown").otherwise(col("brand_name"))
)
df_clean = df_clean.withColumn(
    "brand_url", when(col("brand_url").isNull(), "unknown").otherwise(col("brand_url"))
)
# Handle null/empty brand columns 

df_clean.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(output_gcs_path)
# Save as CSV to GCS

