from flask_blog import app
from flask import request, redirect, url_for, render_template, flash, session
from functools import wraps

# ログイン確認のデコレーター


def login_required(view):
    # fuctools.wrapを読み込むことでdocstringの不整合を防ぐ
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

# 404エラー
@app.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('login'))
# ログイン
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザー名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            flash('ログインしました')
            session['logged_in'] = True
            return redirect(url_for('entry.show_entries'))

    return render_template('login.html')
# ログアウト
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('entry.show_entries'))
