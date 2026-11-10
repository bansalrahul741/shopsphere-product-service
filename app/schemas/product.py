from pydantic import BaseModel, ConfigDict, Field


# Schema for creating a product
class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    description: str = Field(max_length=500)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


# Schema for updating a product
class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    price: float | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)


# Schema for returning product details
class ProductResponse(ProductCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)