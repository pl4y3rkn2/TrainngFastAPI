from pydantic import BaseModel
from pydantic import Field

class Product(BaseModel):
    name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="apple"
        )
    price: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="20"
        )