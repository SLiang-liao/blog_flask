from time import sleep,localtime
'''返回当地时间(str)'''
def get_time():
    
    tm=localtime()[0:6]
    tm=[str(x) for x in tm]
    return tm[0]+':'+tm[1]+':'+tm[2]+':'+tm[3]+':'+tm[4]+':'+tm[5]
