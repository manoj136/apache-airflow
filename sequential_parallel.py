from datetime import timedelta

from airflow.models import DAG
from airflow import AirflowException
from airflow.operators.python_operator import PythonOperator


def first_task_callable():
    print("First DAG task executed Successfully!!")
    
def second_task_callable():
    print("Second DAG task executed Successfully!!")


def third_task_callable():
    print("Third DAG task executed Successfully!!")
    
def fourth_task_callable():
    print("Fourth DAG task executed Successfully!!")

dag = DAG(dag_id="sequential_parallel_dag")

first_task = PythonOperator(
    dag=dag,
    task_id="first_task",
    python_callable=first_task_callable
)

second_task = PythonOperator(
    dag=dag,
    task_id="second_task",
    python_callable=second_task_callable
)

third_task = PythonOperator(
    dag=dag,
    task_id="third_task",
    python_callable=third_task_callable
)

fourth_task = PythonOperator(
    dag=dag,
    task_id="fourth_task",
    python_callable=fourth_task_callable
)

first_task >> [second_task, third_task] >> fourth_task