from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Choisir l'URL de la base de données en fonction de l'environnement
DATABASE_URL = os.getenv("DATABASE_URL")

# Connexion SQLAlchemy
engine = create_engine(DATABASE_URL)
meta = MetaData()
con = engine.connect()

# Tester la connexion (optionnel)
print(f"Connected to the database: {DATABASE_URL}")
