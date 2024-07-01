from airflow.models import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

dag = DAG(dag_id="child_workflow_dag")

child_dag_trigger = TriggerDagRunOperator(
  dag=dag,
  task_id="child_dag_trigger",
  trigger_dag_id="Simple_Dag",
  conf={"notice": "Hello DAG!"}
)

child_dag_trigger
