from marshmallow import Schema, fields


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Pluck(GenreSchema, 'name')
    director = fields.Pluck(DirectorSchema, 'name')


movies_schema = MovieSchema(many=True)
director_schema = DirectorSchema(many=True)
genre_schema = GenreSchema(many=True)
