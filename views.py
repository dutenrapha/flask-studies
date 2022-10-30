def init_app(app):
    """Extensions factory initialization"""

    @app.route("/")
    def index():
        return("<h1>Hello World!</h1>")