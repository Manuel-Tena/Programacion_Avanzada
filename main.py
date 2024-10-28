from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from movies import MovieModel
from random import randint
from sqlmodel import select
from schemas import MovieSchema

app = FastAPI()

create_db_and_tables()

@app.post("/movies")
async def create_movie(movie_data: MovieSchema, database: SessionDep):
    movie = MovieModel(MovieName=movie_data.MovieName, ReleaseYear=movie_data.ReleaseYear, Duration=movie_data.Duration, Director=movie_data.Director, Classification=movie_data.Classification, Gender=movie_data.Gender)
    database.add(movie)
    database.commit()
    database.refresh(movie)
    return movie

@app.get("/movies")
async def get_movies(database: SessionDep):
    statement = select(MovieModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/movies/{movie_id}")
async def get_movie_by_id(movie_id: int, database: SessionDep):
    movie = database.get(MovieModel, movie_id)
    if not movie:
        return HTTPException(status_code=404, detail="Pelicula no encontrada")
    return movie