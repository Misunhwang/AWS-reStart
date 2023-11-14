from pydantic import BaseModel, field_validator

class BookItem(BaseModel):
    name : str
    author : str
    year_published : int

    @field_validator("year_published")
    @classmethod
    def check_valid_country(cls, year_published: int):
        assert year_published <= 2023, "year_published must not be over than 2023"
        assert year_published > (2023-3000), "year_published must be greater than (2023-3000)"
        return year_published
