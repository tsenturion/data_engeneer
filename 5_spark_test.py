# spark_test.py (альтернативная версия)

from pyspark.sql import SparkSession

# Создаём SparkSession без обратных слешей
spark = (SparkSession.builder
         .appName("VSCodeSparkWindowsTest")
         .master("local[*]")
         .getOrCreate())

# Пример данных
data = [("Анна", 28), ("Иван", 35), ("Мария", 22)]
columns = ["Имя", "Возраст"]

# Создаём DataFrame
df = spark.createDataFrame(data, columns)

# Выводим результат
df.show()
df.printSchema()

# Останавливаем Spark
spark.stop()