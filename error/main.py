# # # # # # from fastapi import FastAPI, Depends, HTTPException
# # # # # # from pydantic import BaseModel, ValidationError
# # # # # # from sqlalchemy import Column, Integer, String, create_engine
# # # # # # from sqlalchemy.ext.declarative import declarative_base
# # # # # # from sqlalchemy.orm import sessionmaker, Session

# # # # # # # Database setup (SQLite for simplicity)
# # # # # # DATABASE_URL = "sqlite:///./test.db"  # Change this to any other DB if you need

# # # # # # # Create the SQLAlchemy engine
# # # # # # engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# # # # # # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # # # # # # Base class for SQLAlchemy models
# # # # # # Base = declarative_base()

# # # # # # # SQLAlchemy ORM model (this represents the "users" table)
# # # # # # class User(Base):
# # # # # #     __tablename__ = 'users'

# # # # # #     id = Column(Integer, primary_key=True, index=True)
# # # # # #     name = Column(String, index=True)
# # # # # #     email = Column(String, unique=True, index=True)

# # # # # #     def __repr__(self):
# # # # # #         return f"User(id={self.id}, name={self.name}, email={self.email})"

# # # # # # # Custom function to check for missing orm_mode=True in Pydantic models
# # # # # # def check_orm_mode(pydantic_model: BaseModel):
# # # # # #     if not hasattr(pydantic_model.Config, "orm_mode") or not pydantic_model.Config.orm_mode:
# # # # # #         raise HTTPException(
# # # # # #             status_code=500,
# # # # # #             detail="Pydantic model missing `orm_mode=True`. Please include it in your model's Config class."
# # # # # #         )

# # # # # # # Pydantic schema for response (with `orm_mode=True`)
# # # # # # class UserOut(BaseModel):
# # # # # #     id: int
# # # # # #     name: str
# # # # # #     email: str

# # # # # #     class Config:
# # # # # #         orm_mode = True  # We expect `orm_mode` to be True here.

# # # # # # # Pydantic schema for request (creating new user)
# # # # # # class UserCreate(BaseModel):
# # # # # #     name: str
# # # # # #     email: str

# # # # # #     class Config:
# # # # # #         orm_mode = True

# # # # # # # FastAPI app initialization
# # # # # # app = FastAPI()

# # # # # # # Dependency to get the database session
# # # # # # def get_db():
# # # # # #     db = SessionLocal()
# # # # # #     try:
# # # # # #         yield db
# # # # # #     finally:
# # # # # #         db.close()

# # # # # # # Create the database tables (if not already created)
# # # # # # Base.metadata.create_all(bind=engine)

# # # # # # # Route to get a user by ID
# # # # # # @app.get("/users/{user_id}", response_model=UserOut)
# # # # # # async def get_user(user_id: int, db: Session = Depends(get_db)):
# # # # # #     # Check if the response model has `orm_mode=True` before serializing
# # # # # #     check_orm_mode(UserOut)

# # # # # #     # Query the user from the database
# # # # # #     user = db.query(User).filter(User.id == user_id).first()
# # # # # #     if user is None:
# # # # # #         raise HTTPException(status_code=404, detail="User not found")
# # # # # #     return user  # Return the user (FastAPI will use the Pydantic model to serialize it)

# # # # # # # Route to create a new user (for testing purposes)
# # # # # # @app.post("/users/", response_model=UserOut)
# # # # # # async def create_user(user: UserCreate, db: Session = Depends(get_db)):
# # # # # #     # Check if the response model has `orm_mode=True` before serializing
# # # # # #     check_orm_mode(UserOut)

# # # # # #     db_user = User(name=user.name, email=user.email)
# # # # # #     db.add(db_user)
# # # # # #     db.commit()
# # # # # #     db.refresh(db_user)
# # # # # #     return db_user  # Return the newly created user


# # # # # from fastapi import FastAPI, Depends, HTTPException
# # # # # from pydantic import BaseModel, ValidationError
# # # # # from sqlalchemy import Column, Integer, String, create_engine
# # # # # from sqlalchemy.ext.declarative import declarative_base
# # # # # from sqlalchemy.orm import sessionmaker, Session


# # # # # # Database setup (SQLite for simplicity)
# # # # # DATABASE_URL = "sqlite:///./test.db"  # Change this to any other DB if you need

# # # # # # Create the SQLAlchemy engine
# # # # # engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# # # # # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # # # # # Base class for SQLAlchemy models
# # # # # Base = declarative_base()

# # # # # # SQLAlchemy ORM model (this represents the "users" table)
# # # # # class User(Base):
# # # # #     __tablename__ = 'users'

# # # # #     id = Column(Integer, primary_key=True, index=True)
# # # # #     name = Column(String, index=True)
# # # # #     email = Column(String, unique=True, index=True)

# # # # #     def __repr__(self):
# # # # #         return f"User(id={self.id}, name={self.name}, email={self.email})"


# # # # # # Global Pydantic Base Model that forces `orm_mode=True`
# # # # # class BaseModelWithORM(BaseModel):
# # # # #     class Config:
# # # # #         orm_mode = False


# # # # # # FastAPI app initialization
# # # # # app = FastAPI()

# # # # # # Dependency to get the database session
# # # # # def get_db():
# # # # #     db = SessionLocal()
# # # # #     try:
# # # # #         yield db
# # # # #     finally:
# # # # #         db.close()


# # # # # # Create the database tables (if not already created)
# # # # # Base.metadata.create_all(bind=engine)


# # # # # # Pydantic schema for response using the global base model
# # # # # class UserOut(BaseModelWithORM):
# # # # #     id: int
# # # # #     name: str
# # # # #     email: str


# # # # # # Pydantic schema for request (creating new user)
# # # # # class UserCreate(BaseModelWithORM):
# # # # #     name: str
# # # # #     email: str


# # # # # # Route to get a user by ID
# # # # # @app.get("/users/{user_id}", response_model=UserOut)
# # # # # async def get_user(user_id: int, db: Session = Depends(get_db)):
# # # # #     # Query the user from the database
# # # # #     user = db.query(User).filter(User.id == user_id).first()
# # # # #     if user is None:
# # # # #         raise HTTPException(status_code=404, detail="User not found")
# # # # #     return user  # Return the user (FastAPI will use the Pydantic model to serialize it)


# # # # # # Route to create a new user (for testing purposes)
# # # # # @app.post("/users/", response_model=UserOut)
# # # # # async def create_user(user: UserCreate, db: Session = Depends(get_db)):
# # # # #     db_user = User(name=user.name, email=user.email)
# # # # #     db.add(db_user)
# # # # #     db.commit()
# # # # #     db.refresh(db_user)
# # # # #     return db_user  # Return the newly created user


# # # # from fastapi import FastAPI, Depends, HTTPException
# # # # from pydantic import BaseModel
# # # # from sqlalchemy import Column, Integer, String, create_engine
# # # # from sqlalchemy.ext.declarative import declarative_base
# # # # from sqlalchemy.orm import sessionmaker, Session

# # # # # Database setup (SQLite for simplicity)
# # # # DATABASE_URL = "sqlite:///./test.db"  # Change this to any other DB if needed

# # # # # Create the SQLAlchemy engine
# # # # engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# # # # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # # # # Base class for SQLAlchemy models
# # # # Base = declarative_base()

# # # # # SQLAlchemy ORM model (this represents the "users" table)
# # # # class User(Base):
# # # #     __tablename__ = 'users'

# # # #     id = Column(Integer, primary_key=True, index=True)
# # # #     name = Column(String, index=True)
# # # #     email = Column(String, unique=True, index=True)

# # # #     def __repr__(self):
# # # #         return f"User(id={self.id}, name={self.name}, email={self.email})"

# # # # # FastAPI app initialization
# # # # app = FastAPI()

# # # # # Dependency to get the database session
# # # # def get_db():
# # # #     db = SessionLocal()
# # # #     try:
# # # #         yield db
# # # #     finally:
# # # #         db.close()

# # # # # Create the database tables (if not already created)
# # # # Base.metadata.create_all(bind=engine)

# # # # # Pydantic schema for response (with `orm_mode=True` to handle SQLAlchemy ORM objects)
# # # # class UserOut(BaseModel):
# # # #     id: int
# # # #     name: str
# # # #     email: str

# # # #     # class Config:
# # # #     #     orm_mode = True  # This tells Pydantic to handle SQLAlchemy ORM objects

# # # # # Pydantic schema for request (creating a new user)
# # # # class UserCreate(BaseModel):
# # # #     name: str
# # # #     email: str

# # # #     class Config:
# # # #         orm_mode = True  # This tells Pydantic to handle SQLAlchemy ORM objects

# # # # # Route to get a user by ID
# # # # @app.get("/users/{user_id}", response_model=UserOut)
# # # # async def get_user(user_id: int, db: Session = Depends(get_db)):
# # # #     # Query the user from the database
# # # #     user = db.query(User).filter(User.id == user_id).first()
# # # #     if user is None:
# # # #         raise HTTPException(status_code=404, detail="User not found")
# # # #     return user  # FastAPI will automatically use UserOut to serialize the response

# # # # # Route to create a new user (for testing purposes)
# # # # @app.post("/users/", response_model=UserOut)
# # # # async def create_user(user: UserCreate, db: Session = Depends(get_db)):
# # # #     db_user = User(name=user.name, email=user.email)
# # # #     db.add(db_user)
# # # #     db.commit()
# # # #     db.refresh(db_user)
# # # #     return db_user  # FastAPI will automatically use UserOut to serialize the response


# # # from fastapi import FastAPI, Depends, HTTPException
# # # from pydantic import BaseModel
# # # from sqlalchemy import Column, Integer, String, create_engine
# # # from sqlalchemy.ext.declarative import declarative_base
# # # from sqlalchemy.orm import sessionmaker, Session

# # # # Database setup (SQLite for simplicity)
# # # DATABASE_URL = "sqlite:///./test.db"  # Change this to any other DB if needed

# # # # Create the SQLAlchemy engine
# # # engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# # # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # # # Base class for SQLAlchemy models
# # # Base = declarative_base()

# # # # SQLAlchemy ORM model (this represents the "users" table)
# # # class User(Base):
# # #     __tablename__ = 'users'

# # #     id = Column(Integer, primary_key=True, index=True)
# # #     name = Column(String, index=True)
# # #     email = Column(String, unique=True, index=True)

# # #     def __repr__(self):
# # #         return f"User(id={self.id}, name={self.name}, email={self.email})"

# # # # FastAPI app initialization
# # # app = FastAPI()

# # # # Dependency to get the database session
# # # def get_db():
# # #     db = SessionLocal()
# # #     try:
# # #         yield db
# # #     finally:
# # #         db.close()

# # # # Create the database tables (if not already created)
# # # Base.metadata.create_all(bind=engine)

# # # # Pydantic schema for response (without `orm_mode=True`)
# # # class UserOut(BaseModel):
# # #     id: int
# # #     name: str
# # #     email: str

# # #     # `orm_mode=False` (default) does NOT handle SQLAlchemy ORM models automatically
# # #     class Config:
# # #         orm_mode = False  # No automatic conversion of SQLAlchemy models to dicts

# # # # Pydantic schema for request (creating a new user)
# # # class UserCreate(BaseModel):
# # #     name: str
# # #     email: str

# # #     class Config:
# # #         orm_mode = False  # This is the default value (doesn't handle ORM objects)

# # # # Route to get a user by ID
# # # @app.get("/users/{user_id}", response_model=UserOut)
# # # async def get_user(user_id: int, db: Session = Depends(get_db)):
# # #     # Query the user from the database
# # #     user = db.query(User).filter(User.id == user_id).first()
# # #     if user is None:
# # #         raise HTTPException(status_code=404, detail="User not found")
    
# # #     # Here, FastAPI will try to use `UserOut` to serialize the `user` (which is a SQLAlchemy ORM object).
# # #     # Since `orm_mode=False`, it will not know how to convert the SQLAlchemy object to a dict and will raise an error.
# # #     return user  # This will raise an error

# # # # Route to create a new user (for testing purposes)
# # # @app.post("/users/", response_model=UserOut)
# # # async def create_user(user: UserCreate, db: Session = Depends(get_db)):
# # #     db_user = User(name=user.name, email=user.email)
# # #     db.add(db_user)
# # #     db.commit()
# # #     db.refresh(db_user)

# # #     # Here as well, FastAPI will try to serialize `db_user`, and it will fail because of `orm_mode=False`.
# # #     return db_user  # This will also raise an error

# # from fastapi import FastAPI, Depends, HTTPException
# # from pydantic import BaseModel
# # from sqlalchemy import Column, Integer, String, create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker, Session


# # DATABASE_URL = "sqlite:///./test.db" 

# # engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# # Base = declarative_base()


# # class User(Base):
# #     __tablename__ = 'users'

# #     id = Column(Integer, primary_key=True, index=True)
# #     name = Column(String, index=True)
# #     email = Column(String, unique=True, index=True)

# #     def __repr__(self):
# #         return f"User(id={self.id}, name={self.name}, email={self.email})"


# # app = FastAPI()


# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()


# # Base.metadata.create_all(bind=engine)

# # class UserOut(BaseModel):
# #     id: int
# #     name: str
# #     email: str

# #     # class Config:
# #     #     orm_mode = True  

# # class UserCreate(BaseModel):
# #     name: str
# #     email: str

# #     # class Config:
# #     #     orm_mode = True


# # @app.get("/users/{user_id}", response_model=UserOut)
# # async def get_user(user_id: int, db: Session = Depends(get_db)):
# #     user = db.query(User).filter(User.id == user_id).first()
# #     if user is None:
# #         raise HTTPException(status_code=404, detail="User not found")
# #     return user  

# # @app.post("/users/", response_model=UserOut)
# # async def create_user(user: UserCreate, db: Session = Depends(get_db)):
# #     db_user = User(name=user.name, email=user.email)
# #     db.add(db_user)
# #     db.commit()
# #     db.refresh(db_user)
# #     return db_user 


# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel
# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session

# # Database Configuration
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # SQLAlchemy Model
# class User(Base):
#     __tablename__ = 'users'
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)

#     def __repr__(self):
#         return f"User(id={self.id}, name={self.name}, email={self.email})"

# # FastAPI Application
# app = FastAPI()

# # Dependency to get database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Create Database Tables
# Base.metadata.create_all(bind=engine)

# # Pydantic Models (Without orm_mode)
# class UserOut(BaseModel):
#     id: int
#     name: str
#     email: str

# class UserCreate(BaseModel):
#     name: str
#     email: str

# # API Endpoints
# @app.get("/users/{user_id}")
# async def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     # Manually convert SQLAlchemy object to dictionary
#     # return {"id": user.id, "name": user.name, "email": user.email}
#     return user

# @app.post("/users/")
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(name=user.name, email=user.email)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
    
#     # Manually convert SQLAlchemy object to dictionary
#     # return {"id": db_user.id, "name": db_user.name, "email": db_user.email}
#     return db_user


# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel
# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session

# # Database Configuration
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # SQLAlchemy Model
# class User(Base):
#     __tablename__ = 'users'
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)

#     def __repr__(self):
#         return f"User(id={self.id}, name={self.name}, email={self.email})"

# # FastAPI Application
# app = FastAPI()

# # Dependency to get database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Create Database Tables
# Base.metadata.create_all(bind=engine)

# # Pydantic Models (Without orm_mode)
# class UserOut(BaseModel):
#     id: int
#     name: str
#     email: str

# class UserCreate(BaseModel):
#     name: str
#     email: str

# # API Endpoints

# @app.get("/users/{user_id}")
# async def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     # Manually convert SQLAlchemy object to dictionary
#     return user

# @app.post("/users/")
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     print(f"Type of user before DB insert: {type(user)}")  # Debugging output
    
#     # Convert Pydantic model to SQLAlchemy ORM model
#     db_user = User(name=user.name, email=user.email)
    
#     print(f"Type of db_user after conversion: {type(db_user)}")  # Debugging output
    
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)

#     print(f"Type of db_user after DB insert: {type(db_user)}")  # Debugging output

#     # Manually convert SQLAlchemy object to dictionary
#     return db_user


# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel
# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session

# # -------------------- Database Setup --------------------
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # -------------------- SQLAlchemy Model --------------------
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     phone = Column(String, nullable=True)

# # -------------------- Create DB Table --------------------
# Base.metadata.create_all(bind=engine)

# # -------------------- Pydantic Models (Without orm_mode) --------------------
# class UserCreate(BaseModel):
#     name: str
#     email: str
#     phone: str

# class UserOut(BaseModel):
#     id: int
#     name: str
#     email: str
#     phone: str  # ✅ this will trigger the error when `orm_mode` is missing

#     # ❌ orm_mode is intentionally NOT set here to cause an error
#     # class Config:
#     #     orm_mode = True

# # -------------------- FastAPI App --------------------
# app = FastAPI()

# # -------------------- Dependency --------------------
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # -------------------- Routes --------------------
# @app.post("/users/", response_model=UserOut)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(name=user.name, email=user.email, phone=user.phone)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user  # ⛔ ORM object returned directly, no orm_mode — this will fail

# @app.get("/users/{user_id}", response_model=UserOut)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user  # ⛔ Again, returning ORM object without orm_mode

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# -------------------- Database Setup --------------------
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# -------------------- SQLAlchemy Model --------------------
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)

# Create DB Table
Base.metadata.create_all(bind=engine)

# -------------------- Pydantic Models --------------------
class UserCreate(BaseModel):
    name: str
    email: str
    phone: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    extra_field: str  # ⛔ This field does NOT exist in ORM model

    # ❌ orm_mode is missing
    class Config:
        orm_mode = True

# -------------------- FastAPI App --------------------
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create User
@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  # ⛔ This will now fail

# Get User
@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user  # ⛔ This will now also fail
