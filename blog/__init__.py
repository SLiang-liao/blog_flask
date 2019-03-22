import os
from flask import Flask

app = Flask(__name__)
SECRET_KEY = os.getenv("SECRET_KEY") or "1"


DATABASE = os.path.join(app.root_path+'/models/', 'db.db')#app.root_path为__init__.py所在的文件夹(blog)

app.config.from_object(__name__)

from blog.api import views