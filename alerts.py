from airflow import DAG 
from datetime import datetime
from airflow.operators.email import EmailOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 7, 2),
}

dag = DAG('send_alert_dag', default_args=default_args, schedule_interval='@daily')

send_email = EmailOperator(
    task_id='send_email',
    email_conn_id='SMTP_Connection',
    to='mkumar@valethi.in',
    subject='Airflow Alert',
    html_content='<p>Your Airflow job has finished.</p>',
    dag=dag
)

send_email
