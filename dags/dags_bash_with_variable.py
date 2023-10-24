from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from airflow.models import Variable

with DAG(
    dag_id="dags_bash_with_variable",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    var_value = Variable.get("sample_key")

    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command=f"echo variable: {var_value}",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo variable: {{ var.value.sample_key }}",
    )

    bash_t1 >> bash_t2
