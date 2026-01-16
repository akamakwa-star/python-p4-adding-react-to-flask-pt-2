
from app import app
from models import db, Movie

with app.app_context():
    db.create_all()
    # Seed data
    movie_list = [
        Movie(title="The Matrix"),
        Movie(title="Inception"),
        Movie(title="Interstellar")
    ]
    db.session.add_all(movie_list)
    db.session.commit()
    print("Database seeded!")
