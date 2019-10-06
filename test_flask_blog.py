import os
import flask_blog
from flask_blog.views import views
from flask_blog.views.entries import entry
# ユニットテストのモジュールインポート
import unittest

import tempfile
from flask_blog.scripts.db import InitDB

flask_blog.app.register_blueprint(entry, url_prefix='/users')
# テスト用のクラスを生成（テストケースクラスを継承）


class TestFlaskBlog(unittest.TestCase):
    # テストを実行するときに最初に実行される関数
    def setUp(self):
        self.db_fd, flask_blog.DATABASE = tempfile.mkstemp()
        self.app = flask_blog.app.test_client()
        InitDB().run()
    # テストの終了直前に実行されるメソッド
    # データベースをきれいにする

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flask_blog.DATABASE)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password

        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
    # test_というプレフィックスでテスト自動s実行

    def test_login_logout(self):
        rv = self.login('john', 'due123')
        # print(rv.data)
        assert 'ログインしました'.encode() in rv.data
        rv = self.logout()
        assert 'ログアウトしました'.encode() in rv.data
        rv = self.login('admin', 'default')
        assert 'ユーザー名が異なります'.encode() in rv.data
        rv = self.login('john', 'defaultx')
        # print(rv.data.decode())
        assert 'パスワードが異なります'.encode() in rv.data


if __name__ == '__main__':
    unittest.main()
