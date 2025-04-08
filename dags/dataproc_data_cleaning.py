from datetime import datetime
from airflow import models
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator

# DAG config
PROJECT_ID = "project_id"
REGION = "europe-west1"
CLUSTER_NAME = "cluster-name"

# PySpark script location
PYSPARK_URI = "gs://My-bucket/Scripts/Spark_Batch_processing.py"

# Default args
default_args = {
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with models.DAG(
    dag_id="dataproc_data_cleaning_dag",
    schedule_interval=None, 
    default_args=default_args,
    catchup=False,
    tags=["dataproc", "pyspark", "gcs"],
) as dag:

    dataproc_job = {
        "reference": {"project_id": PROJECT_ID},
        "placement": {"cluster_name": CLUSTER_NAME},
        "pyspark_job": {
            "main_python_file_uri": PYSPARK_URI,
        },
    }

    submit_job = DataprocSubmitJobOperator(
        task_id="run_pyspark_cleaning_job",
        job=dataproc_job,
        region=REGION,
        project_id=PROJECT_ID,
    )
