#!/usr/bin/env python
# coding: utf-8
import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine
from prefect import task, flow
from prefect.tasks import task_input_hash
from datetime import timedelta


@task(log_prints=True)
def extract_data(url, retried=3, cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1)):
     # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    if url.endswith('.csv.gz'):
        csv_name = 'yellow_tripdata_2021-01.csv.gz'
    else:
        csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")
  

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    return df


@task(log_prints=True)
def transform_data(df):
    print(f"pri:missing passanger {df['passenger_count'].isin([0]).sum()}")
    df = df[df['passenger_count']!=0]
    print(f"post: missing passanger {df['passenger_count'].isin([0]).sum()}")
    return df


@task(log_prints=True, retries=1)
def ingest_data(user, password, host, port, db, table_name, df):
    postgress_url = (f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine = create_engine(postgress_url)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')

@flow(name="subflow", log_prints=True)
def log_subflow(table_name:str):
    print("logging subflow {table_name}")

@flow(name="ingest flow")
def main(table_name : str):
    user = "root"
    password = "root"
    host = "localhost"
    port = "5432"
    db = "ny_taxi"
    csv_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
    log_subflow(table_name)
    raw_data = extract_data(csv_url)
    data = transform_data(raw_data)
    ingest_data(user, password, host, port, db, table_name, data)
if __name__== '__main__':
    main("yellow_taxi_trips")