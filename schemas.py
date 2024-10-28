from pydantic import BaseModel
from datetime import datetime

class MovieSchema(BaseModel):
    MovieName: str
    ReleaseYear: str
    Duration: str   
    Director: str   
    Classification: str
    Gender: str