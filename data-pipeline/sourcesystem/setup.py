# Databricks notebook source
# MAGIC %md
# MAGIC Execute desired portions of this notebook for ingesting / updating / removing data source information from the system.

# COMMAND ----------

# DBTITLE 1,Create delta table for sources
from delta.tables import *

DeltaTable.createIfNotExists(spark) \
  .addColumn("format", "STRING") \
  .addColumn("schema", "STRING") \
  .addColumn("path", "STRING") \
  .property("description", "Sources information") \
  .location("/tmp/project/sources/delta/sources") \
  .execute()

# COMMAND ----------

# DBTITLE 1,Troubleshoot: Remove source delta table
# Uncomment for troubleshoot
#dbutils.fs.rm("/tmp/project/sources/delta/sources", True)
