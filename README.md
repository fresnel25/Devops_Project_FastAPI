# `DevOps FastAPI Project`

Ce projet est une API REST simple de gestion d'objets **items** construite avec `FastAPI`, connectée à une base de données `PostgreSQL`. Elle est accompagnée de bonnes pratiques DevOps : CI/CD avec GitHub Actions, tests unitaires avec `pytest`, analyse de sécurité et de style avec `bandit` et `flake8`, ainsi que le déploiement sur `Render`.

---

## `Fonctionnalités`

- CRUD complet pour les objets `items`
- Documentation  avec `Swagger`
- Sécurité de base avec `bandit`
- Linting du code avec `flake8`
- Pipeline CI avec `GitHub Actions`
- Tests automatisés avec `pytest`
- Déploiement continu sur `Render`

---

## `Installation locale`

#### Cloner le dépôt

    git clone https://github.com/ton-repo/devops_fastapi_project.git
    
    cd devops_fastapi_project
---

#### Configurer l'environnement

Créer un fichier .env à la racine :

    DATABASE_URL=postgresql://DB_USER:DB_PASSWORD@localhost/DB_NAME

---
#### Installer les dépendances

    python -m venv venv <!-- creation variariable d'environnement -->

    source venv/bin/activate <!-- activer la variariable d'environnement -->

    pip install -r requirements.txt 

#### Lancer l'application :

    uvicorn main:app --reload

    Accès Swagger : http://localhost:8000/docs

## `Tests`
Les tests unitaires se trouvent dans le dossier tests/ :

    pytest

## `Analyse de qualité et sécurité`
flake8 (qualité du code) :

    flake8 .
bandit (analyse sécurité) :

    bandit -r .

## `CI/CD avec GitHub Actions`

Un pipeline CI est configuré dans 

    .github/workflows/ci-cd.yml

Le pipeline s'exécute automatiquement à chaque push ou pull_request sur la branche main.

## `Déploiement`

Le déploiement est effectué automatiquement sur Render après validation CI. Voici une capture d'écran (à remplacer) :


## `Exemples d'Endpoints`

Méthode	URL	Description

    GET	/api/getallitems	Récupère tous les items

    GET	/api/getitem/{id}	Récupère un item par ID

    POST	/api/createitem	Crée un nouvel item

    PUT	/api/edititem/{id}	Met à jour un item
    
    DELETE	/api/deleteitem/{id}	Supprime un item









