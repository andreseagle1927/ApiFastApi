from pydantic import BaseModel
from datetime import datetime
#s
class StudentSchema(BaseModel):
    Id: int
    FirstName: str
    LastName: str
    DateOfBirth: datetime
    Sex: str

