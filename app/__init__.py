from flask import Flask, render_template
from flask_login import LoginManager
# from .database import init_engine, init_db, db_session
from .models import User

# from .home.views import mod as main_blueprint
# from .users.views import mod as user_blueprint
from .main.views import main as main_app


login_manager = LoginManager()


def create_app(db_uri='any'):

    app = Flask(__name__)
    app.config.from_object('app.default_config')
    # app.config.from_pyfile(os.path.join(app.instance_path, 'config.py'))

    app.register_blueprint(main_app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')

    @app.errorhandler(500)
    def internal_error(exception):
        app.logger.exception(exception)
        return "Some Internal error has taken place."

    return app


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
