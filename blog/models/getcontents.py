from blog.models.blogDB import get_db
import hashlib

class Contents:
    def __init__(self):
        self.__db=get_db()
        self.__cur=self.__db.cursor()
        self.__cur.execute("SELECT * from sqlite_master ")
        self.__db_tables=self.__cur.fetchall()
        if self.__db_tables==None:
            self.__cur.execute("CREATE TABLE articles(id INT NOT NULL,title CHAR NOT NULL,contents CHAR NOT NULL,date CHAR NOT NULL,tags CHAR NOT NULL)")
            self.__db.commit()
        
        
        
    def get_article_byid(self,id):
        self.__cur.execute("SELECT * from articles where id =?",(id,))
        temp=self.__cur.fetchall()[0]
        return dict(zip(('id','title','contents','date','tags'),temp))

    def get_articles(self):
        temp=self.__cur.execute("select *from articles order by id DESC")
        temp=self.__cur.fetchall()
        get=[]
        for each in temp:
            get.append(dict(zip(('id','title','contents','date','tags'),each)))
        return get
    def  get_shares(self):
        temp=self.__cur.execute("select *from shares order by id DESC")
        temp=self.__cur.fetchall()
        get=[]
        for each in temp:
            get.append(dict(zip(('id','url','pwd','tags','contents'),each)))
        return get

