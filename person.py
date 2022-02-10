from redis_om import (Field, HashModel)
from pydantic import PositiveInt

class Person(HashModel):
    # Indexed for exact text matching
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)

    # Indexed for numeric matching
    age: PositiveInt = Field(index=True)

    # Indexed for full text search
    personal_statement: str = Field(index=True, full_text_search=True)

    # Geolocation (not yet supported in Redis OM Python
    # TODO