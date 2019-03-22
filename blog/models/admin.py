from blog.models.blogDB import get_db
import hashlib
class Admin:
    def __init__(self):
        self.__db=get_db()
        self.__cur=self.__db.cursor()
        self.__pwd=[]
        self.__adminname=[]
    def post_article(self,id,title,contents,date,tags):
        self.__cur.execute("insert into articles(id,title,contents,date,tags)values(?,?,?,?,?)",(id,title,contents,date,tags))
        self.__db.commit()
    def get_articlesnum(self):
        self.__cur.execute("select articlesnum from admin")
        num=int(self.__cur.fetchall()[0][0])
        self.__cur.execute("update admin set articlesnum=?",(num+1,))
        return num+1
    def verify(self,adminname,password):
        temp=hashlib.md5(password.encode('utf-8')).hexdigest()+'31415926'#两次加密
        temp=hashlib.md5(temp.encode('utf-8')).hexdigest()
        
        self.__cur.execute("select adminname from admin")
        self.__adminname=self.__cur.fetchall()[0][0]
        self.__cur.execute("select password from admin")
        if temp==self.__cur.fetchall()[0][0] and adminname==self.__adminname:
            return '1'
        else:
            return '0'
    def comment(self,name,email,comments,date):
        self.__cur.execute("insert into comments(name,emailadd,comments,date)VALUES(?,?,?,?)",(name,email,comments,date))
        self.__db.commit()
