from redis_om import (EmbeddedJsonModel, Field, JsonModel)
from pydantic import PositiveInt
from typing import Optional, List

class Address(EmbeddedJsonModel):
    street_number: PositiveInt = Field(index=True)

    # Unit isn't in all addresses, so let's make it optional...
    unit: Optional[str] = Field(index=True)
    street_name: str = Field(index=True)
    city: str = Field(index=True)
    state: Optional[str] = Field(index=True)
    postal_code: str = Field(index=True)

    # Provide a default value if none supplied...
    country: str = Field(index=True, default="United Kingdom")

class Person(JsonModel):
    # Indexed for exact text matching
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)

    # Indexed for numeric matching
    age: PositiveInt = Field(index=True)

    # Use an embedded sub-model
    address: Address

    skills: List[str] = Field(index=True)

    # Indexed for full text search
    personal_statement: str = Field(index=True, full_text_search=True)
