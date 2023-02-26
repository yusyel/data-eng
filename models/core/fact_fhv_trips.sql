{{ config(materialized='table') }}

with green_data as (
    select *, 
        'Green' as service_type 
    from {{ ref('stg_green_tripdata') }}
), 

yellow_data as (
    select *, 
…dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)