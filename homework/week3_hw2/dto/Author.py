from pydantic import BaseModel, field_validator
import re

def match_regex1(input_str:str) -> bool:
    test_results = re.search(r"^[A-Z][a-z]* [A-Z][a-z]*$", input_str)
    return test_results != None

def match_regex2(input_str:str) -> bool:
    test_results = re.search(r"[A-Z]{4}-[0-9]{4}", input_str)
    return test_results != None and len(input_str) == 9

class Author(BaseModel):
    name: str
    author_id: str

    @field_validator("name")
    @classmethod
    def check_valid_name(cls, name: str):
        assert match_regex1(name), "author name must be like 'John Doe'"
        return name
    
    @field_validator("author_id")
    @classmethod
    def check_valid_author_id(cls, author_id: str):
        assert match_regex2(author_id), "author id must have format 'XXXX-YYYY, X is capital letter and Y is number"
        return author_id
