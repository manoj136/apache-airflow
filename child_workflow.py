from airflow.models import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

dag = DAG(dag_id="manual_intervention_approval_dag")

child_dag_trigger = TriggerDagRunOperator(
  dag=dag,
  task_id="child_dag_trigger",
  trigger_dag_id="Simple_Dag",
  conf={"notice": "Hello DAG!"}
)

child_dag_trigger