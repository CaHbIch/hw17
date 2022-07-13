from flask import request
from flask_restx import Resource, Namespace

from implement import movies_dao

movies_ns = Namespace('movies')
director_ns = Namespace('directors')
genre_ns = Namespace('genres')


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        if director_id and genre_id:
            return movies_dao.get_director_and_genre(director_id, genre_id)
        if director_id:
            return movies_dao.get_one_director(director_id), 200
        if genre_id:
            return movies_dao.get_one_genre(genre_id), 200
        return movies_dao.get_alL_movies(), 200


@movies_ns.route("/<int:pk>")
class MoviesView(Resource):
    def get(self, pk):
        return movies_dao.get_one_movie(pk), 200


@director_ns.route("/")
class MoviesView(Resource):
    def get(self):
        return movies_dao.all_director_movie()

    def post(self):
        return f'Режиссер  добавлен', movies_dao.add_director()


@director_ns.route("/<int:pk>")
class MoviesView(Resource):
    def get(self, pk):
        return movies_dao.get_one_director(pk), 200

    def put(self, pk):
        return f"Режиссер  обновлен", movies_dao.update_director(pk)

    def delete(self, pk):
        return f"Режисер удален", movies_dao.delete_director(pk)

@genre_ns.route("/")
class MoviesView(Resource):
    def get(self):
        return movies_dao.all_genre_movie(), 200


@genre_ns.route("/<int:pk>")
class MoviesView(Resource):
    def get(self, pk):
        return movies_dao.get_one_genre(pk), 200
