from flask import Flask
from routes import book_blueprint
from models import db, init_app, Book
from flask_migrate import Migrate

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NxU7k9N3oz_8hr2TMn_2sg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(book_blueprint)

# Define the database URI
database_file = os.path.join(os.getcwd(), 'database', 'book.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_file}'

# Ensure the database directory exists
os.makedirs(os.path.dirname(database_file), exist_ok=True)

init_app(app)

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True, port=5002)