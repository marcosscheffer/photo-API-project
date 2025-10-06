# 🧩 Flask RESTful Project Framework

**Base framework for building RESTful APIs with Flask**, designed to streamline project setup and enforce consistent best practices in professional development environments.

---

## 🚀 Main Features

✅ Modular and scalable layered architecture  
✅ Flask + SQLAlchemy + Flask-Migrate + Marshmallow  
✅ Environment variable support (`python-dotenv`)  
✅ Built-in `/health` route for quick status check  
✅ Supports MySQL (via `PyMySQL`) and SQLite (for development)  

---

## 🧱 Project Structure

```
flask-restful-project-framework/
│
├── run.py                      → Application entry point
├── app/
│   ├── __init__.py             → App Factory + blueprint and CLI registration
│   ├── config.py               → Environment and configuration settings
│   ├── extensions.py           → db, migrate, and marshmallow initialization
│   │
│   ├── views/                  → Routes and endpoints (Blueprints)
│   │   ├── __init__.py
│   │   └── health_view.py
│   │
│   ├── models/                 → Database models (SQLAlchemy)
│   ├── schemas/                → Serialization and validation (Marshmallow)
│   ├── services/               → Business logic layer
│   ├── validations/            → Input validation
│   └── entities/               → Domain entities (optional)
│
├── requirements.txt            → Project dependencies
├── .flaskenv                   → Flask configuration (dev)
├── .env                        → Sensitive variables (do not version)
├── .gitignore                  → Git ignore file
└── README.md                   → This file
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/marcosscheffer/flask-restful-project-framework.git
cd flask-restful-project-framework
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
# source venv/bin/activate  (Linux/Mac)
pip install -r requirements.txt
```

### 3️⃣ Configure the `.env` file
Create a `.env` file in the project root with database credentials and secret key:
```
SECRET_KEY=dev-key
DATABASE_URL=mysql+pymysql://user:password@localhost/dev_db?charset=utf8mb4
```

> 💡 You can also use SQLite for development:
> ```
> DATABASE_URL=sqlite:///app.db
> ```

---

## ▶️ Running the Project

### Initialize the database
```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```

### Run the server
```bash
flask run
```

Access: [http://127.0.0.1:5000/health](http://127.0.0.1:5000/health)

---

## 🧩 Using this Framework for New Projects

### 🧱 Option 1 — Clone manually
```bash
git clone https://github.com/marcosscheffer/flask-restful-project-framework.git
```

### 🧱 Option 2 — Use as a GitHub Template
1. On GitHub, click **“Use this template”**.  
2. Create a new repository with your project name.  
3. Clone it and start developing 🚀

---

## 📦 Core Dependencies
| Package | Purpose |
|----------|----------|
| **Flask** | Main web framework |
| **Flask-SQLAlchemy** | ORM integration |
| **Flask-Migrate** | Database migrations |
| **Flask-Marshmallow** | Serialization & validation |
| **PyMySQL** | MySQL driver |
| **python-dotenv** | Environment variable loader |
---

## 💡 Future Improvements
- ✅ JWT Authentication support  
- ✅ Logging and error handling system  
- ✅ Docker support (`Dockerfile`, `docker-compose.yml`)  
- ✅ CI/CD setup (GitHub Actions)  

---

**Author:** [@marcosscheffer](https://github.com/marcosscheffer)  
📧 Contact: *marcosscheffer2989@gmail.com*
