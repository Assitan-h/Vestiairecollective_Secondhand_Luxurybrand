from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2025, 4, 5),
}

dag = DAG(
    'load_csv_to_bq',
    default_args=default_args,
    description='Load CSV data from GCS to BigQuery',
    schedule_interval='@monthly', 
    # Run monthly
    catchup=False,
)

# Task : Load data from GCS to BigQuery
load_csv_to_bq = GCSToBigQueryOperator(
    task_id='load_csv_to_bq',
    bucket='My-bucket-name',  
    source_objects=["data/processed/vestiaire_cleaned.csv/*.csv"], 
    destination_project_dataset_table="project_id:dataset_table"
    ,
    source_format='CSV',  
    skip_leading_rows=1, 
    # Skip header row in CSV
    field_delimiter=',',  
    create_disposition='CREATE_IF_NEEDED', 
    # Create table if it doesn't exist
    write_disposition='WRITE_TRUNCATE', 
    # Overwrite table
    dag=dag,
)

load_csv_to_bq
