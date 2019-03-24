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

    def get_idforarticle(self,tags):
        self.__cur.execute("select * from admin")
        numlist=self.__cur.fetchall()[0][2:]
        if tags=='Python':
            index=2
        elif tags=='MachineLearning':
            index=3
        elif tags=='Other':
            index=4
        else:
            index=5

        self.__cur.execute("update admin set "+tags+" = ? ,articlesnum = ?",(int(numlist[index])+1,int(numlist[0])+1))
        self.__db.commit()
        return int(numlist[0])+1

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
    def comment(self,name,contact,comments,date):
        self.__cur.execute("insert into comments(name,contact,comments,date)VALUES(?,?,?,?)",(name,contact,comments,date))
        self.__db.commit()

