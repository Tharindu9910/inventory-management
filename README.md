# Mini Inventory Management System

## Tech Stack

- Python 3.11+
- Django
- PostgreSQL
- uv package manager
- Django ORM

---

## Clone the Project

```bash
git clone <repository-url>
cd inventory-management-system
```

---

## Install Dependencies

This project uses **uv** as the package manager.

```bash
uv sync
```

---

## Environment Configuration

Create a `.env` file using `.env.example`.

## Database Setup (PostgreSQL)

Login to PostgreSQL and run the following SQL commands:

```sql
CREATE DATABASE inventory_db;
CREATE USER inventory_user WITH PASSWORD 'strong_password';

GRANT ALL PRIVILEGES ON DATABASE inventory_db TO inventory_user;
GRANT ALL ON SCHEMA public TO inventory_user;
```

---

## Apply Database Migrations

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Start Dev Server

```bash
uv run python manage.py runserver
```

---

## Access Application

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

