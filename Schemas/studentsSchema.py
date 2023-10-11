from pydantic import BaseModel
from datetime import datetim
class StudentSchema(BaseModel):
    Id: int
    FirstName: str
    LastName: str
    DateOfBirth: datetime
    Sex: str

