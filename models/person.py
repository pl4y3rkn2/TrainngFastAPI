from pydantic import BaseModel
from pydantic import Field

class Person(BaseModel):
    name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="Kevin"
        )
    email: str = Field(
        ...,
        min_length=1,
        max_length=255,
        example="kevinechenique18@gmail.com"
    )