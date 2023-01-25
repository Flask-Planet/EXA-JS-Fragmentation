from flask import Flask

from .views.fragments import fragment_views
from .views.index import index_views


def create_app():
    app = Flask(__name__)

    index_views(app)
    fragment_views(app)

    return app
