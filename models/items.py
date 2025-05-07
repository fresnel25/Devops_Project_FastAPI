from config.db import meta
from sqlalchemy import Table, Column, func
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime, Float

items = Table(
    "items",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("price", Float, nullable=False),
    Column("in_stock", Boolean, default=True),
    Column("quantity", Integer, nullable=False),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),  # suivi modification
)
