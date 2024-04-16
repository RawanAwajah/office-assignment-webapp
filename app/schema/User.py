# app/schema/user_schema.py
from typing import Optional
from pydantic import BaseModel

# User base schema including common attributes
class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    role: str
    department_id: Optional[int] = None

# Schema for creating a new user (without ID, which is auto-generated by the database)
class UserCreate(UserBase):
    password: str  # This will be the plain password provided during user creation

# Schema for reading user data including the ID (for response model use)
class UserRead(UserBase):
    id: int  # ID is included for reading, as it will be provided by the database

    class Config:
        orm_mode = True  # This configuration is required for Pydantic to read data from ORM models

# Schema for updating user data (all fields are optional)
class UserUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None
    department_id: Optional[int] = None
    password: Optional[str] = None  # In case you want to provide functionality to update the password