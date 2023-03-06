# Databricks notebook source
raw_zone_path="/mnt/rawdata"
checkpoint_location= raw_zone_path + "/checkpoint"

# COMMAND ----------

from typing import List

allowed_formats = ["csv"]

for frmt in allowed_formats:
    spark.read.format(frmt).load(raw_zone_path + "/" + frmt + "/*/*." + frmt).write.format("delta").option("mode", "append").mode("overwrite").save("/tmp/project/framework/datahub-zone/")


# COMMAND ----------

spark.read.format("delta").load("/tmp/project/framework/datahub-zone/").show()
