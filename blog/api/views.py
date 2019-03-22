from flask import render_template, url_for,request
from blog import app
from blog.models.getcontents import Contents
from blog.api.gettime import get_time
from blog.models.admin import Admin

@app.route('/')
def index():
        get=Contents()
        return  render_template('index.html',articles=get.get_articles())


@app.route('/wati.html')
def wait():
        return render_template('wati.html')


@app.route('/article<id>')
def get_full_read(id):
        get=Contents()
        return render_template('article.html',article=get.get_article_byid(int(id)))

@app.route('/articles_list')
def get_articles_list():
        get=Contents()
        return render_template('articles.html',articles=get.get_articles())
@app.route('/edit',methods=['get'])
def postarticle():
        return render_template('edit.html')
@app.route('/submitok.html',methods=['post'])
def post_ok():
        admin=Admin()
        id=admin.get_articlesnum()
        title=request.form.get('title')
        contents=request.form.get('contents')
        tags=request.form.get('tags')
        date=get_time()
        admin.post_article(id,title,contents,date,tags)

        return render_template('submitok.html')

@app.route('/edit.html')
def  get_edit_page():
        return render_template('edit.html')

@app.route('/login.html')
def login():
        return render_template('login.html')

@app.route('/admin.html',methods=['post'])
def login_ok():
        admin=Admin()
        adminname=request.form.get('adminname')
        password=request.form.get('password')
        if  admin.verify(adminname,password)=='1':
                return render_template('admin.html')
        return render_template('loginfail.html')


@app.route('/shares.html')
def get_shares():
        get=Contents()
        return render_template('shares.html',shares=get.get_shares())


@app.route('/messageboard.html')
def post_message():
        return render_template('messageboard.html')


@app.route('/commentok',methods=['post'])
def comment_ok():
        admin=Admin()
        name=request.form.get('name')
        emailadd=request.form.get('email')
        comments=request.form.get('comments')
        date=get_time()
        admin.comment(name,emailadd,comments,date)
        return render_template('submitok.html')
        