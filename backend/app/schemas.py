from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class SubmissionBase(BaseModel):
    image_path: str
    extracted_text: Optional[str] = None
    analysis_result: Optional[str] = None
    grade: Optional[float] = None

class SubmissionCreate(SubmissionBase):
    user_id: int

class Submission(SubmissionBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None 