from pydantic import BaseModel, Field


class PersonBase(BaseModel):
    """
    Base schema with common person attributes.
    """
    firstName: str = Field(..., example="John")
    lastName: str = Field(..., example="Doe")
    dni: str = Field(..., example="12345678A")
    birthProvince: str = Field(..., example="Madrid")


class PersonCreate(PersonBase):
    """
    Schema used when creating a new person via POST /person. Equal to PersonBase, created for legibility.
    """
    pass


class PersonRead(PersonBase):
    """
    Schema used when returning a person to the client.
    Must include the primary key.
    """
    id: int

    class Config:
        from_attributes = True
