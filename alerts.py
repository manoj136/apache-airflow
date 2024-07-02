from airflow import DAG 
from airflow.operators.email import EmailOperator

dag = DAG('send_alert_dag', schedule_interval='@daily')

send_email = EmailOperator(
    task_id='send_email',
    to='mkumar@valethi.in',
    subject='Airflow Alert',
    html_content='<p>Your Airflow job has finished.</p>',
    dag=dag
)

send_email
