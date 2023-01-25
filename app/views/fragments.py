from flask import render_template


def fragment_views(app):
    @app.route('/frag-cars')
    def frag_cars():
        cars = [
            {"make": "Ford", "model": "Fiesta"},
            {"make": "Ford", "model": "Focus"},
            {"make": "Ford", "model": "Mustang"},
            {"make": "Ford", "model": "Ranger"},
        ]
        return render_template(
            "frag:cars.html",
            cars=cars
        )
