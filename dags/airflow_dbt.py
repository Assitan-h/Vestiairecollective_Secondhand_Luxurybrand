from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2025, 4, 5),
}

dag = DAG(
    'dbt_transformation_dag',
    default_args=default_args,
    description='Run DBT transformations',
    schedule_interval=None,  
    catchup=False,
)

dbt_run = BashOperator(
    task_id='run_dbt',
    bash_command='cd ~/my_dbt_project/my_vestiaire && dbt run',
    dag=dag,
)

dbt_run
