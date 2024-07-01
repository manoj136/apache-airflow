from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 7, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('user_input_script_dag',
         default_args=default_args,
         schedule_interval='@daily') as dag:

    run_script = BashOperator(
        task_id='run_script',
        bash_command='echo {{ params.input }} ',
        params={'input': 'your_input'},
    )