# minimal_spark_test.py



try:
    from pyspark.sql import SparkSession
    
    # Максимально простой SparkSession
    spark = SparkSession.builder \
        .appName("MinimalTest") \
        .master("local[1]") \
        .getOrCreate()
    
    print("✅ Spark запущен!")
    
    # Самый простой DataFrame
    df = spark.createDataFrame([(1, "test")], ["id", "name"])
    df.show()
    
    spark.stop()
    print("✅ Успех!")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")