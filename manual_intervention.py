from datetime import timedelta

from airflow.models import DAG
from airflow import AirflowException
from airflow.operators.python_operator import PythonOperator

from my_tasks import first_task_callable, second_task_callable


TIMEOUT = timedelta(days=14)


def task_to_fail():
    raise AirflowException("Please change this step to success to continue")


dag = DAG(dag_id="my_dag")

first_task = PythonOperator(
    dag=dag,
    task_id="first_task",
    python_callable=first_task_callable
)

manual_sign_off = PythonOperator(
    dag=dag,
    task_id="manual_sign_off",
    python_callable=task_to_fail,
    retries=1,
    max_retry_delay=TIMEOUT
)

second_task = PythonOperator(
    dag=dag,
    task_id="second_task",
    python_callable=second_task_callable
)

first_task >> manual_sign_off >> second_task