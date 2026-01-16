from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import db, Movie
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

CORS(app)

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return make_response(jsonify([movie.to_dict() for movie in movies]), 200)

if __name__ == '__main__':
    app.run(port=5555)
