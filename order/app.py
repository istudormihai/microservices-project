from flask import Flask
from routes import order_blueprint
from models import db, init_app
from flask_migrate import Migrate
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '7avUhoZcq56FTCFDeb5nEZ'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database_file = os.path.join(os.getcwd(), 'database', 'order.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_file}'

os.makedirs(os.path.dirname(database_file), exist_ok=True)

init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(order_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
