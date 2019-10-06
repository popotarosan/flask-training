from flask import request,redirect,url_for,render_template,flash,session
from flask_blog import app
from flask_blog.models.entries import Entry
# __init__で定義
from flask_blog import db
@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        # url_forでメソッド指定でリダイレクトする
        return redirect(url_for('login'))
    #Entryモデルからクエリで取得
    entries = Entry.query.order_by(Entry.id.desc()).all()

    return render_template('entries/index.html',entries=entries)

@app.route('/entries/new',methods=['GET'])
def new_entry():
    # ログイン状態でしか新規投稿はできない
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('entries/new.html')

@app.route('/entries',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    # entriesモデルのインスタンスをformからの値を元に生成
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>',methods=['GET'])
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/show.html',entry=entry)
# 編集画面表示
@app.route('/entries/<int:id>/edit',methods=['GET'])
def edit_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/edit.html',entry=entry)

# 更新
@app.route('/entries/<int:id>/update',methods=['POST'])
def update_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

