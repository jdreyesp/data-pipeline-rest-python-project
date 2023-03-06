# Databricks notebook source
# Add role to SP from Azure CLI
# az role assignment create --assignee "2e18e478-0b56-4000-99f4-f2c43006a5cb" --role "ba92f5b4-2d11-453d-a403-e96b0029c9fe" --subscription "d263242b-5bc5-41f6-9d8c-f1881a3ed70b"

# Set up connection with ADLS
dbutils.fs.unmount("/mnt/rawdata")

configs = {"fs.azure.account.auth.type": "OAuth",
       "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
       "fs.azure.account.oauth2.client.id": "2e18e478-0b56-4000-99f4-f2c43006a5cb",
       "fs.azure.account.oauth2.client.secret": "-kk8Q~i-unU3wcT0e_5Rv0l2cQgjli1vvfOCRaSL", #This should be stored in KV
       "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/0ef60589-2312-4218-b9c5-db8f74d091ab/oauth2/token",
       "fs.azure.createRemoteFileSystemDuringInitialization": "true"}

dbutils.fs.mount(
source = "abfss://raw@nnrawzone.dfs.core.windows.net/raw",
mount_point = "/mnt/rawdata",
extra_configs = configs)
