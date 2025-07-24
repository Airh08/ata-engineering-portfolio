import os
import logging
from sqlalchemy import create_engine, text
import pytest

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Config
DB_USER = os.getenv("DB_USER", "ecommerce_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "ecommerce_password")
DB_NAME = os.getenv("DB_NAME", "ecommerce_db")
DB_HOST = os.getenv("DB_HOST", "localhost")

logger.info("Starting test script...")

# Database URL
logger.info("URL of DB...")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

@pytest.fixture(scope="module")
def engine():
    engine = create_engine(DATABASE_URL)
    yield engine
    engine.dispose()

# Validaciones de nulos
def test_no_null_customers(engine):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT COUNT(*) FROM customers 
            WHERE customer_id IS NULL OR name IS NULL
        """)).scalar()
        assert result == 0, f"Clientes con datos nulos: {result}"

def test_no_null_sales(engine):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT COUNT(*) FROM sales 
            WHERE customer_id IS NULL OR product_id IS NULL 
            OR store_id IS NULL OR time_id IS NULL
        """)).scalar()
        assert result == 0, f"Ventas con llaves nulas: {result}"


# Validaciones de integridad referencial
def test_sales_customers_integrity(engine):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT COUNT(*) FROM sales s
            LEFT JOIN customers c ON s.customer_id = c.customer_id
            WHERE c.customer_id IS NULL
        """)).scalar()
        assert result == 0, f"Ventas con customer_id inválido: {result}"

def test_sales_products_integrity(engine):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT COUNT(*) FROM sales s
            LEFT JOIN products p ON s.product_id = p.product_id
            WHERE p.product_id IS NULL
        """)).scalar()
        assert result == 0, f"Ventas con product_id inválido: {result}"

def test_sales_stores_integrity(engine):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT COUNT(*) FROM sales s
            LEFT JOIN stores st ON s.store_id = st.store_id
            WHERE st.store_id IS NULL
        """)).scalar()
        assert result == 0, f"Ventas con store_id inválido: {result}"

def test_sales_time_integrity(engine):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT COUNT(*) FROM sales s
            LEFT JOIN time t ON s.time_id = t.time_id
            WHERE t.time_id IS NULL
        """)).scalar()
        assert result == 0, f"Ventas con time_id inválido: {result}"