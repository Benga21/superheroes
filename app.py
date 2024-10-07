from flask import Flask
from database import db
from routes import configure_routes

def create_app(config_name=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if config_name == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_superheroes.db'
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    configure_routes(app)
    @app.route('/')
    def home():
        return "Welcome to the Superheroes API!"
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
