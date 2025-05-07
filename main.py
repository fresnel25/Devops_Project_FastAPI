from fastapi import FastAPI
from routes.index import routes
from config.db import engine, meta


app = FastAPI()

# Crée toutes les tables associées à meta
meta.create_all(engine)

for route in routes:
    app.include_router(route)
