from flask import Flask
import settings
from app01.user import db
from app01.user.view import user_bp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    # app.config['DEBUG'] = True
    db.init_app(app)
    app.register_blueprint(user_bp)
    print(app.url_map)
    # print(app.config)
    return app
