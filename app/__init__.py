from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager
from .models import User


from .main.views import main as main_app


login_manager = LoginManager()


def create_app(db_uri='any'):

    app = Flask(__name__)
    app.config.from_object('app.default_config')
    # app.config.from_pyfile(os.path.join(app.instance_path, 'config.py'))

    @app.route('/')
    def index():
        return redirect(url_for('main.home'))

    app.register_blueprint(main_app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')

    @app.errorhandler(500)
    def internal_error(exception):
        app.logger.exception(exception)
        return "Some Internal error has taken place."


    @app.after_request
    def add_security_headers(resp):
        # resp.headers['Content-Security-Policy']="default-src 'self' style-src 'self' 'unsafe-inline'; img-src 'self' data:;"     #OLD
        # resp.headers['Content-Security-Policy']="default-src https:; object-src 'none'"

        # resp.headers['X-Content-Type-Options'] = 'nosniff' #Habilitar para servidor
        # resp.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains';#OJO
        # resp.headers['X-XSS-Protection'] = '1; mode=block'
        #resp.headers['Content-Security-Policy']="frame-ancestors 'none';"
        #resp.headers['X-Frame-Options'] = 'DENY'
        resp.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
        return resp

    return app


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
