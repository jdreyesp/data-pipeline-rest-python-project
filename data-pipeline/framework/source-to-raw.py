# Databricks notebook source
sources_path="/tmp/project/sources/delta/sources"
raw_zone_path="/mnt/rawdata"
checkpoint_location= raw_zone_path + "/checkpoint"

# COMMAND ----------

from pyspark.sql import Row
from delta.tables import DeltaTable
from typing import Dict, List
from collections import defaultdict
import uuid

uids_by_format_dict = defaultdict(list)
allowed_formats = ["csv"]
    
# First part of the pipeline
def sources_to_raw(sources_dict: Dict) -> None: 
    for source in sources_dict:
        source_format = source.get("format")
        if any(source_format in s for s in allowed_formats):
            out_name = str(uuid.uuid4()) # Source ID will be a random UID, but it could also come from a possible ID column from the source system, if we need to track which source correspond with which files in ADLSGen2
            write_from_format(source_format, source.get("schema"), source.get("path"), out_name)
            
def write_from_format(source_format: str, source_schema: str, source_path: str, out_name: str) -> None:
    if source_format == "csv":
        spark.read.format(source_format).load(source_path).write.format(source_format).save(raw_zone_path + "/" + source_format + "/" + out_name)
    # more formats go here 

dt = DeltaTable.forPath(spark, sources_path)
sources_dict: Dict = dt.toDF().toPandas().to_dict(orient="records")

sources_to_raw(sources_dict)
