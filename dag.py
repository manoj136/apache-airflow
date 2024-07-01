#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Manoj Kumar
"""

from airflow import DAG
from datetime import datetime

# Define the DAG
dag = DAG(
    dag_id="test_dag",
    description="just dag!'",
    start_date=datetime(2024, 6, 27),
    schedule_interval="@daily",
    catchup=False,
)

dag
#########################################

###########################################
