from datetime import datetime,timedelta 

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'soheil',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is our first dag',
    start_date=datetime(2025, 7, 20, 2),
    schedule='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world"
    )

    task2 = BashOperator(
        task_id= 'second_task',
        bash_command= 'echo second task is running'
    )

    task3 = BashOperator(
        task_id= 'third_task',
        bash_command= "echo I am thethird task"
    )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    task1 >> [task2, task3]