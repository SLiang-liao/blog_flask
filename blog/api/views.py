from flask import render_template, url_for,request,redirect,abort,Response
from blog import app
from blog.models.getcontents import Contents
from blog.api.gettime import get_time
from blog.models.admin import Admin

@app.route('/')#进入主页渲染主页内容
def index():
        get=Contents()
        return  render_template('index.html',articles=get.get_articles(),nums=get.get_numlist())
@app.route('/articles_list') #自动得到文章列表
def get_articles_list():
        get=Contents()
        return render_template('articles.html',articles=get.get_articles())
<<<<<<< HEAD

@app.route('/deletearticles')
def get_articles_manage():
        get=Contents()
        return render_template('articles_manage.html',articles=get.get_articles())

=======
>>>>>>> afbfceda5267265790b461a1138a0820191a1412
@app.route('/cate<tags>')
def get_articles_bytags(tags):
        get=Contents()
        return render_template('classified_by_tags.html',articles=get.get_articles_bytags(tags),nums=get.get_numlist())


@app.route('/article<id>')#获得文章的编号为id的全部内容
def get_full_read(id):
        get=Contents()
        return render_template('article.html',article=get.get_article_byid(int(id)) ,nums=get.get_numlist())



@app.route('/submitok.html',methods=['post'])
def post_ok(): #文章的上传处理 即表单action的目的地
        admin=Admin()
        
        title=request.form.get('title')
        contents=request.form.get('contents')
        tags=request.form.get('tags')
        id=admin.get_idforarticle(tags)
        date=get_time()
        admin.post_article(id,title,contents,date,tags)

        return render_template('ok.html')

@app.route('/edit.html') #获得文本编辑器的路由
def  get_edit_page():
        return render_template('editor.html')#取得编辑文章页面

@app.route('/login.html') #渲染登陆界面
def login():
        return render_template('login.html')

@app.route('/admin.html',methods=['post'])#验证登录信息
def login_ok():
        admin=Admin()
        adminname=request.form.get('adminname')
        password=request.form.get('password')
        if  admin.verify(adminname,password)=='1':
                return render_template('admin.html')
        return render_template('loginfail.html')


@app.route('/shares.html')   #渲染分享界面
def get_shares():
        get=Contents()
        return render_template('shares.html',shares=get.get_shares())


@app.route('/messageboard.html')  #留言面板
def post_message():
        get=Contents()
        return render_template('messageboard.html',commentswell=get.get_comments_well())


@app.route('/commentok',methods=['post']) #留言上传
def comment_ok():
        admin=Admin()
        
        name=request.form.get('name')
        contact=request.form.get('contact')
        comments=request.form.get('comments')
        if comments=='':
                abort(Response("留言不能为空哦"))
        date=get_time()
        admin.comment(name,contact,comments,date)
        return redirect(url_for('commentswell'))
@app.route('/comentswell')
def commentswell():
        get=Contents()
        return render_template('messageboard.html',commentswell=get.get_comments_well())
<<<<<<< HEAD
@app.route('/adminhome')
def admin():
        return render_template('admin.html')
        
@app.route('/deleteok',methods=['post'])
def deleteok():
        id=request.form.get('id')
        tags=request.form.get('tags')
        admin=Admin()
        admin.deletearticles(id,tags)
        return redirect(url_for('get_articles_manage'))

=======
>>>>>>> afbfceda5267265790b461a1138a0820191a1412

@app.route('/wati.html')#t通用等待页面。提示功能正在开发中。
def wait():
        return render_template('wati.html')