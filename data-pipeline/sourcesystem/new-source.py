# Databricks notebook source
sources_path="/tmp/project/sources/delta/sources"

# COMMAND ----------

# DBTITLE 1,New source
import pandas as pd

data = [['csv', None, '/tmp/project/ingest/source1/data.csv']]
df = pd.DataFrame(data, columns = ['format', 'schema', 'path']) 

spark.createDataFrame(df).write.format("delta").mode("append").save(sources_path)


# COMMAND ----------

# DBTITLE 1,Display current sources
display(spark.read.format("delta").load(sources_path))
