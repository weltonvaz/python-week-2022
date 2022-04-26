from email.policy import default
from tokenize import ContStr
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select, insert, update, delete

class Beer(SQLModel, table=True):
    id: Optional(int) = Field(int, primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    Cont: int

    @validator("flavor", "image", "Cont")
    def validate_rating(cls, v, field):
        if v < 1 or v > 10:
            raise ValueError(f'{field.name} must be between 1 and 10')
        return v

try:
    brewdog = Beer(name="BrewDog", style="NEIPA", flavor=5, image=8, Cont=8)
except RuntimeError:
    print("Zica de mais ")