from airflow import DAG
from datetime import datetime
from airflow.operators.http_operator import SimpleHttpOperator

def handle_response(response):
    if response.status_code==200:
        print("recieved 200 OK")
        return True
    else:
        print("error")
        return False
    


with DAG('weatherServiceCall', start_date=datetime(2024, 7, 2), schedule_interval="*/5 * * * *") as dag:
    task = SimpleHttpOperator(
        task_id='weaatherApi',
        method='GET',
        http_conn_id='weather_api',
        endpoint='/weather/NewYork',
        headers={"Content-Type": "application/json"},
        response_check= lambda response: handle_response(response), 
        dag=dag)

task