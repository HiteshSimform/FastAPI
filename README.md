# FastAPI

---

## ✅ **README Template for FastAPI - Day 1 - 29-04-2025**

You can name the file something like:

```
fastapi-learning-log/README.md
```

---

### 📅 **Day 1: FastAPI Introduction & Setup**

#### 🔰 Topics Covered:
- What is FastAPI?
- Key Features of FastAPI
- FastAPI vs Flask vs Django (short comparison)
- Installing FastAPI & Uvicorn
- First “Hello World” FastAPI app
- Running FastAPI app with Uvicorn
- Auto-generated Swagger UI and Redoc
- Project directory structure (basic layout)

---

### 🛠️ **Commands Used Today:**

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install FastAPI and Uvicorn
pip install fastapi uvicorn

# Run FastAPI app
uvicorn main:app --reload
```

---

### 📂 **Project Structure:**
```
fastapi-learning/
├── main.py
├── venv/
└── README.md
```

---

### 📜 **Code Sample – `main.py`:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}!"}
```

---

### 📘 **Concept Notes:**

- `FastAPI()` creates the application instance.
- `@app.get("/path")` is used to define route handlers.
- `uvicorn main:app --reload`:
  - `main`: filename (main.py)
  - `app`: FastAPI app object
  - `--reload`: auto-reload server on code changes
- OpenAPI documentation available at:
  - `/docs` (Swagger UI)
  - `/redoc` (ReDoc)

---

### 🧠 **Things I Learned Today:**

- FastAPI is **type-hint driven**, making development easier and docs automatic.
- Much faster than Flask due to Starlette + Pydantic.
- First-class async support.

---