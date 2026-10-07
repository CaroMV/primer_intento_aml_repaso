#TODAS LAS CLASES IMPORTAN MYSQLCONNECTION
from flask_app.config.mysqlconnection import connectToMySQL

class Pelicula:

    #metodo constructor
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.director = data.get('director')
        self.fecha_estreno = data.get('fecha_estreno')
        self.sinopsis = data.get('sinopsis')

        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.usuario_id=data.get('usuario_id')

    #para guardar 1 registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO peliculas (nombre, director, fecha_estreno, sinopsis, created_at, updated_at, usuario_id) VALUES (%(nombre)s, %(director)s, %(fecha_estreno)s,%(sinopsis)s, NOW(), NOW(), %(usuario_id)s)"

        return connectToMySQL('cinepedia').query_db(query, data)

    #metodo para ver todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM peliculas"

        peliculas_en_db = connectToMySQL('cinepedia').query_db(query)
    
        peliculas = []
        for pelicula in peliculas_en_db:
            peliculas.append(cls(pelicula))

        return peliculas


    #metodo para ver 1 registro
    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM peliculas WHERE id = %(id)s;"
        pelicula_en_db = connectToMySQL('cinepedia').query_db(query,datos)

        return cls(pelicula_en_db[0])

    #metodo para editar registro
    @classmethod
    def update(cls, datos):
        query = "UPDATE peliculas SET nombre=%(nombre)s, director=%(director)s, fecha_estreno=%(fecha_estreno)s, sinopsis=%(sinopsis)s,updated_at=NOW(), usuario_id=%(usuario_id)s WHERE id = %(id)s;"

        return connectToMySQL('cinepedia').query_db(query, datos)
    

    #metodo para eliminar registro
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM peliculas WHERE id = %(id)s;"
        return connectToMySQL('cinepedia').query_db(query, datos)