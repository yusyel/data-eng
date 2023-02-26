{{ config(materialized='view') }}




select count(*) from  {{source('staging', 'fhv_tripdata')}}
