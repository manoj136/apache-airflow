from datetime import timedelta

from airflow.models import DAG
from airflow import AirflowException
from airflow.operators.python_operator import PythonOperator


def first_task_callable():
    print("First DAG task executed Successfully!!")
    
def second_task_callable():
    print("Second DAG task executed Successfully!!")


TIMEOUT = timedelta(days=14)


def task_to_fail():
    raise AirflowException("Please change this step to success to continue")


dag = DAG(dag_id="manual_intervention_approval_dag")

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