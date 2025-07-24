with sales as (
    select * from {{ ref('stg_sales') }}
)
select
    sale_id,
    customer_id,
    product_id,
    store_id,
    date_id,
    quantity
from sales
