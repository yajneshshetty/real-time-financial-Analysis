
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("financial_pipeline", start_date=datetime(2025, 1, 1), schedule_interval=None) as dag:
    start_kafka = BashOperator(task_id="start_kafka", bash_command="echo 'Kafka is starting...'")
    start_flink = BashOperator(task_id="start_flink", bash_command="echo 'Flink is starting...'")
    start_superset = BashOperator(task_id="start_superset", bash_command="echo 'Superset is starting...'")
    start_kafka >> start_flink >> start_superset
