from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Himanshu',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

with DAG(
    dag_id='one_task_dag',
    description='A one task Airflow DAG',
    schedule_interval=None,
    default_args=default_args,
    start_date=datetime(2025, 8, 13),
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id='one_task',
        bash_command='echo "hello, linkedin learning!" > /workspaces/hands-on-introduction-data-engineering-4395021/lab'
    )
