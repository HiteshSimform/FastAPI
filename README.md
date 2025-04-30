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

https://chatgpt.com/share/6810a444-f018-8011-9658-3dea6dcedd93


## ✅ **README Template for FastAPI - Day 2 - 30-04-2025**
---

# 📥 Request Body in FastAPI – In-Depth Interview-Level Explanation

In FastAPI, **request bodies** are a key concept used to send structured data (like JSON) to the server, particularly for `POST`, `PUT`, and `PATCH` requests.

---

## 🧠 What is a Request Body?

A **request body** is the part of the HTTP request that contains data **sent by the client** to be **processed by the server**. For example:
- Sending user data during registration
- Submitting a form or JSON payload
- Updating a resource with new information

Unlike **query parameters** or **path parameters** which are part of the URL, the **request body** is sent in the body of the HTTP request.

---

## ✅ How FastAPI Handles Request Bodies

FastAPI uses **Pydantic models** to:
- Validate
- Parse
- Document

incoming request bodies.

### 🔧 Basic Syntax

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created", "age": user.age}
```

### 💡 What Happens Internally?

1. FastAPI reads the body of the request.
2. It parses the JSON into a Python `dict`.
3. It validates the dict against the `User` model using **Pydantic**.
4. If validation fails, it returns a `422 Unprocessable Entity` error.
5. If successful, the data is available as a typed Python object (`user: User`).

---

## 🔍 Interview Deep-Dive

### ❓Q1: Why do we use Pydantic models for request bodies?
**Answer**:  
Pydantic models provide:
- Built-in data validation
- Type safety
- Clean and readable code
- Automatic documentation generation (Swagger/OpenAPI)

They prevent manually writing `if` checks for each input.

---

### ❓Q2: What happens when invalid data is passed?
**Answer**:  
FastAPI returns:
- Status code `422 Unprocessable Entity`
- A detailed JSON error explaining which fields failed and why

```json
{
  "detail": [
    {
      "loc": ["body", "age"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

---

### ❓Q3: Can we have multiple request bodies?
**Answer**:  
Yes, by using multiple Pydantic models and manually extracting fields. However, you **cannot** have multiple top-level bodies. Instead, nest the data.

```python
class Address(BaseModel):
    city: str
    zip: str

class User(BaseModel):
    name: str
    age: int
    address: Address
```

---

### ❓Q4: What about additional metadata or validations?
**Answer**:  
You can use `Field()` from Pydantic for:
- Required fields
- Defaults
- Min/max lengths
- Descriptions (shown in docs)

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="User's full name")
    age: int = Field(gt=0, lt=120, description="User's age")
```

---

### ❓Q5: How are request bodies documented in Swagger UI?
**Answer**:  
FastAPI automatically generates the body schema in **Swagger UI** and **Redoc**, including:
- Field names
- Types
- Validation rules
- Descriptions (if using `Field()`)

---

## 🧪 Advanced Use Cases

### 🧩 Optional Body Parameters

Use `Optional` from `typing` or default values:

```python
from typing import Optional

class User(BaseModel):
    name: str
    bio: Optional[str] = None
```

---

### 🔁 Request Body + Path + Query Parameters

```python
from fastapi import Query

@app.post("/users/{user_id}")
def update_user(user_id: int, user: User, notify: bool = Query(False)):
    return {"id": user_id, "updated": user, "notify": notify}
```

---

### 🔒 Request Body with `Form` or `File`

FastAPI also allows bodies using:
- `Form(...)` for `application/x-www-form-urlencoded`
- `File(...)` for file uploads

---

## 📘 Summary Table

| Concept                      | Description                                                             |
|-----------------------------|-------------------------------------------------------------------------|
| `BaseModel`                 | Defines schema for input validation                                     |
| `Field(...)`                | Adds metadata, constraints, descriptions                                |
| `Optional` / default        | Supports partial updates or optional fields                            |
| `422 Error`                 | Automatic response on failed validation                                |
| Nested Models               | Validates deeply structured JSON payloads                             |
| Swagger Docs                | Auto-generated request body schema                                      |

---

## 🏁 Real-Life Example (Registration API)

```python
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: Optional[str]

@app.post("/register")
def register_user(data: RegisterRequest):
    return {"msg": f"Welcome, {data.full_name or 'user'}!"}
```

---