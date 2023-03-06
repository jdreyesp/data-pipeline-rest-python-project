## Data pipeline as a framework

The data pipeline should be implemented as a deployable and configurable framework that:

- Can be configured to take raw data from multiple sources 
- Copies that data in Azure ADLS Gen2 with raw format
- Applies schema if needed
- Copies the data from ADLS Gen 2 and writes it to Delta Table format

The sources information will be in a Delta table, describing where to take the information from, and additional
data, like source schema (if applies).

The data pipeline framework could be deployed as a Python .egg file in Databricks.

### Requirements

- Azure ADLS Gen2 configured
- Service Principal with Blob Storage Contributor role 
- Databricks workspace

### Source system

Source system is design so that:

- It creates a Delta Table which will be used to insert / fetch sources information.
- A notebook `new-source.py` is provided for helping developers and non-developers for inserting new sources

### Framework

A batch framework has been designed, but read further for streaming pipeline alternative considerations below.

Three main steps of the pipeline:
- `mount-adls.py` will mount the ADLS Gen2 for its use from Databricks
- `source-to-raw.py` is a generic implementation in PySpark that will read from the source Delta Table for sources information. Allowed formats could be extended over time for further sources support
- `raw-to-datahub.py` batch process for fetching data processed in previous step, and write that data into Delta Tables.

#### Streaming pipeline

In case a streaming pipeline is needed, we could make use of `AutoLoader` in `raw-to-datahub.py` so that incoming data
is transferred in an incremental way to the datahub Delta Table. We also could get the benefit of schema evolution supported
by Autoloader.

`raw-to-datahub.py` has no impact on streaming fashion, since we fetch sources information in a batch way. 