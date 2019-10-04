from flask_blog import app
from flask import request,redirect,url_for,render_template,flash,session



@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        # url_forでメソッド指定でリダイレクトする
        return redirect(url_for('login'))
    return render_template('entries/index.html')


# ログイン
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザー名が異なります')
        elif request.form['password'] != app.config['PASSWORD'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            flash('ログインしました')
            session['logged_in'] = True
            return redirect(url_for('show_entries'))
    
    return render_template('login.html')
# ログアウト
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))
