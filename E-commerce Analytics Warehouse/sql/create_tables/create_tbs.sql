CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT,
    category TEXT,
    price NUMERIC(10, 2),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE time (
    time_id SERIAL PRIMARY KEY,
    date DATE,
    day_of_week TEXT,
    month INT,
    year INT
);

CREATE TABLE stores (
    store_id SERIAL PRIMARY KEY,
    name TEXT,
    location TEXT
);

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    product_id INT REFERENCES products(product_id),
    time_id INT REFERENCES time(time_id),
    store_id INT REFERENCES stores(store_id),
    quantity INT,
    total_amount NUMERIC(10, 2)
);
