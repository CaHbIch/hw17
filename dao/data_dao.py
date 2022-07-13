import json

from flask import request

from dao.model.model_movie import Movie, Director, Genre
from dao.model.schemas import movies_schema, director_schema, genre_schema
from setup_db import db


class MoviesDAO:

    def __init__(self, DATABASE):
        self.DATABASE = DATABASE

    def get_alL_movies(self):
        """ Возвращает список всех фильмов, разделенный по страницам """
        all_movie = Movie.query.limit(5).offset(5).all()
        result = movies_schema.dump(all_movie)
        return result

    def get_one_movie(self, pk):
        """ Возвращает подробную информацию о фильме. """
        one_movie = Movie.query.filter(Movie.id == pk)
        result = movies_schema.dump(one_movie)
        return result

    def all_director_movie(self):
        """  Возвращает всех id  режиссера по запросу типа /directors/"""
        movies = Director.query.all()
        result = director_schema.dump(movies)
        return result

    def get_one_director(self, director_id):
        """  Возвращает только режиссера по id """
        movies = Director.query.filter(Director.id == director_id)
        result = director_schema.dump(movies)
        return result

    def all_genre_movie(self):
        """  Возвращает всех id жанра по запросу типа /genres/"""
        movies = Genre.query.all()
        result = genre_schema.dump(movies)
        return result

    def get_one_genre(self, genre_id):
        """  Возвращает только жанр по id """
        movies = Genre.query.filter(Genre.id == genre_id)
        result = genre_schema.dump(movies)
        return result

    def get_director_and_genre(self, director_id, genre_id):
        """ Возвращает только фильмы с определенным режиссером и жанром """
        movies = db.session.query(Movie) \
            .join(Movie.genre) \
            .join(Movie.director) \
            .filter(Movie.genre_id == genre_id, Movie.director_id == director_id) \
            .all()
        result = movies_schema.dump(movies)
        return result

    def add_director(self):
        """ Добавляет режиссера методом POST """
        new_director = Director(**json.loads(request.data))
        db.session.add(new_director)
        return db.session.commit()

    def update_director(self, director_id):
        """ Обновляет данные о режиссере методом PUT """
        director = json.loads(request.data)
        updates_director = db.session.query(Director).filter(Director.id == director_id)
        updates_director.update(director)
        return db.session.commit()

    def delete_director(self, director_id):
        """ Удаляет данные о режиссере """
        director = Director.query.get(director_id)
        db.session.delete(director)
        return db.session.commit()
