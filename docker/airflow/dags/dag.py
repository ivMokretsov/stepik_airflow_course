from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.email_operator import EmailOperator


with DAG(dag_id='dag',
         default_args={'owner': 'airflow'},
         schedule_interval='@daily', # Интервал запусков
         start_date=days_ago(1) # Начальная точка запуска
    ) as dag:

    email_op = EmailOperator(
        task_id='send_email',
        to="ivan.mokretsov@icloud.com",
        subject="Test Email Please Ignore",
        html_content=None
    )

    email_op