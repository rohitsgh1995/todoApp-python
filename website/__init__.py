from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sgusiu763543uy4rfg76384fuyg37u46fg3u4fg3764uy3g48734fguy34'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app