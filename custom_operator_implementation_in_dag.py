from airflow import DAG
from datetime import datetime
from custom_operator import CustomOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 1, 1),
}
dag = DAG('custom_operator_dag', default_args=default_args, schedule_interval='@daily')

custom_task = CustomOperator(
    task_id='custom_task',
    my_param='Thid is custom operator',
    dag=dag)

custom_task