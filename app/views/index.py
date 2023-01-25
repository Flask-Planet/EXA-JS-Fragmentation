from flask import render_template


def index_views(app):
    @app.route('/')
    def index():
        return render_template("index.html")
