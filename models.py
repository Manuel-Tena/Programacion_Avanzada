from sqlmodel import SQLModel, Field
from datetime import datetime

class MovieModel(SQLModel, table=True):
    __tablename__ = "Movies"

    id: int = Field(primary_key=True)
    MovieName: str
    ReleaseYear: str
    Duration: str   
    Director: str   
    Classification: str
    Gender: str
