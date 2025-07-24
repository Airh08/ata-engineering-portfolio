import os
import logging
from faker import Faker
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Date, Numeric
from sqlalchemy.sql import insert
from datetime import datetime, timedelta
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Config
DB_USER = os.getenv("DB_USER", "ecommerce_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "ecommerce_password")
DB_NAME = os.getenv("DB_NAME", "ecommerce_db")
DB_HOST = os.getenv("DB_HOST", "localhost")

logger.info("Starting data generation script...")

# Database URL
logger.info("Connecting to the database...")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# Faker
faker = Faker()
engine = create_engine(DATABASE_URL)
metadata = MetaData()

logger.info("Info schemas and tables...")
# Define tables
customers = Table("customers", metadata,
    Column("customer_id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String),
)

products = Table("products", metadata,
    Column("product_id", Integer, primary_key=True),
    Column("name", String),
    Column("category", String),
    Column("price", Numeric(10, 2)),
)

stores = Table("stores", metadata,
    Column("store_id", Integer, primary_key=True),
    Column("name", String),
    Column("location", String),
)

time = Table("time", metadata,
    Column("time_id", Integer, primary_key=True),
    Column("date", Date),
    Column("day_of_week", String),
    Column("month", Integer),
    Column("year", Integer),
)

sales = Table("sales", metadata,
    Column("sale_id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.customer_id")),
    Column("product_id", Integer, ForeignKey("products.product_id")),
    Column("time_id", Integer, ForeignKey("time.time_id")),
    Column("store_id", Integer, ForeignKey("stores.store_id")),
    Column("quantity", Integer),
    Column("total_amount", Numeric(10, 2)),
)

def seed():
    try:
        logger.info("Seeding data...")
        with engine.connect() as conn:
            logger.info("Inserting customers...")
            conn.execute(insert(customers), [
                {"name": faker.name(), "email": faker.email()}
                for _ in range(100)
            ])

            logger.info("Inserting products...")
            conn.execute(insert(products), [
                {"name": faker.word(), "category": faker.word(), "price": round(random.uniform(10, 200), 2)}
                for _ in range(50)
            ])

            logger.info("Inserting stores...")
            conn.execute(insert(stores), [
                {"name": faker.company(), "location": faker.city()}
                for _ in range(10)
            ])

            logger.info("Inserting time dimension...")
            start_date = datetime(2023, 1, 1)
            time_data = []
            for i in range(365):
                date = start_date + timedelta(days=i)
                time_data.append({
                    "date": date.date(),
                    "day_of_week": date.strftime("%A"),
                    "month": date.month,
                    "year": date.year
                })
            conn.execute(insert(time), time_data)

            logger.info("Inserting sales...")
            sales_data = []
            for _ in range(1000):
                sales_data.append({
                    "customer_id": random.randint(1, 100),
                    "product_id": random.randint(1, 50),
                    "time_id": random.randint(1, 365),
                    "store_id": random.randint(1, 10),
                    "quantity": random.randint(1, 5),
                    "total_amount": round(random.uniform(10, 1000), 2),
                })
            conn.execute(insert(sales), sales_data)
    except Exception as e:
        logger.error("Error connecting to the database: %s", e)
        return None

if __name__ == "__main__":
    seed()
    logger.info("✅ Data generation complete.")
