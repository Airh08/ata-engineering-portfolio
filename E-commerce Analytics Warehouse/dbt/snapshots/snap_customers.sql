{ % snapshot snap_customers % } { { config(
    target_schema = 'snapshots',
    unique_key = 'customer_id',
    strategy = 'check',
    check_cols = ['name', 'email', 'address']
) } }
select
    *
from
    { { source('public', 'customers') } } { % endsnapshot % }