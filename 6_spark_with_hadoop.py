# spark_with_hadoop.py
import os

# Правильная настройка Hadoop
os.environ['HADOOP_HOME'] = 'C:\\Users\\user\\Downloads\\Hadoop'
os.environ['HADOOP_COMMON_HOME'] = 'C:\\Users\\user\\Downloads\\Hadoop'
os.environ['HADOOP_HDFS_HOME'] = 'C:\\Users\\user\\Downloads\\Hadoop'
os.environ['HADOOP_YARN_HOME'] = 'C:\\Users\\user\\Downloads\\Hadoop'
os.environ['HADOOP_MAPRED_HOME'] = 'C:\\Users\\user\\Downloads\\Hadoop'

# Добавляем bin в PATH
hadoop_bin = 'C:\\Users\\user\\Downloads\\Hadoop\\bin'
os.environ['PATH'] = hadoop_bin + ';' + os.environ['PATH']

# Остальные настройки

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HadoopTest") \
    .master("local[*]") \
    .getOrCreate()

# Убираем лишние логи
spark.sparkContext.setLogLevel("ERROR")

data = [("Анна", 28), ("Иван", 35), ("Мария", 22)]
df = spark.createDataFrame(data, ["Имя", "Возраст"])

print("Spark с настроенным Hadoop:")
df.show()

spark.stop()
