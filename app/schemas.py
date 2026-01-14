from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.models import UserRole


class AuthorBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    birth_date: date

    @field_validator("birth_date")
    @classmethod
    def birth_date_not_in_future(cls, v: date) -> date:
        if v > date.today():
            raise ValueError("Birth date cannot be in the future")
        return v


class AuthorCreate(AuthorBase):
    pass


class AuthorResponse(AuthorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    price: int = Field(..., gt=0)
    stock_quantity: int = Field(default=0, ge=0)
    pages: int = Field(..., gt=0)
    genre: str = Field(..., min_length=1, max_length=255)
    author_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    price: int | None = Field(default=None, gt=0)
    stock_quantity: int | None = Field(default=None, ge=0)
    pages: int | None = Field(default=None, gt=0)
    genre: str | None = Field(default=None, min_length=1, max_length=255)


class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    price: int
    stock_quantity: int
    pages: int
    genre: str
    author_id: int
    author: AuthorResponse


class BookListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    price: int
    stock_quantity: int
    pages: int
    genre: str
    author_id: int


class AuthorWithBooksResponse(AuthorResponse):
    books: list[BookListResponse] = []


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    role: UserRole
    creation_date: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: int | None = None


class LoginRequest(BaseModel):
    username: str
    password: str


class OrderCreate(BaseModel):
    book_id: int
    quantity: int = Field(..., gt=0)


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    book_id: int
    quantity: int
    total_price: int
    creation_date: datetime


class PaginatedBooks(BaseModel):
    items: list[BookResponse]
    total: int
    limit: int
    offset: int
