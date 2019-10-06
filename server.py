from flask_blog import app
from flask_blog.views import views
from flask_blog.views.entries import entry


if __name__ == '__main__':
    # entryアプリを登録する
    app.register_blueprint(entry, url_prefix='/users')
    app.run()
