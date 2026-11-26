from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

# -- Models -- #

class Product(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str = Field(index=True, unique=True)
    price: float
    stock: int = 0

class Client(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    phone: str | None = Field(default=None, unique=True)

class Request(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    client_id: int | None = Field(default=None, foreign_key="client.id")
    total: float
    created_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ItemRequest(SQLModel, table=True):
    request_id: int = Field(foreign_key="request.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    quantity: int
    unit_price: float

# -- Schemas -- #

class SearchEntryProduct(SQLModel):
    name: str = Field(min_length=2, max_length=100)

class EntryRequest(SQLModel):
    client_id: int = Field(gt=0)
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0, le=50)