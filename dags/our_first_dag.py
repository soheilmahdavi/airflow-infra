from datetime import datetime,timedelta 

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'soheil',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime(2025, 7, 20, 2),
    schedule='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world"
    )

    task1