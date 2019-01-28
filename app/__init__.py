
import os

try:
    from flask import Flask
    from flask import g
    from flask import current_app
except:
    print("error on loading flask: try to install Flask library", file=sys.stderr)

from app.views import blog
from app.views import blog_post

try:
    from app import settings
except:
    import settings

from app.repository import get_repository_manager

blog_manager = None

def get_manager():
    global blog_manager
    if blog_manager is None:
        blog_manager = get_repository_manager(settings)
        blog_manager.load()
    return blog_manager

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = settings.SECRET

    if test_config is None:
        app.config.from_pyfile('settings.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    with app.app_context():
        current_app.manager = get_manager()
        current_app.running_local = settings.LOCAL

    app.add_url_rule('/', view_func=blog)
    app.add_url_rule('/<string:slug>/', view_func=blog_post)

    return app