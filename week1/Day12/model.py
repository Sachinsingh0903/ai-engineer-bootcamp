from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str
    age: int = Field(gt=0)
    course: str
    marks: float = Field(ge=0, le=100)
    email: str | None = None