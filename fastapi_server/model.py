import pandas as pd
from sqlalchemy import create_engine


dbConn = {
    'host': 'localhost',
    'user': 'root',
    'password': 'yy6689990',
    'db': 'heros',
    'port': 3306
}


class Model():
    def __init__(self):
        # 连接数据库
        self.db = create_engine(
            "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(**dbConn))

    def getHerosByName(self, name: str):
        # 执行sql语句
        sql = f'select * from heros where name like "%%{name}%%";' # 原始sql语句的%需要使用多一个%进行转义
        res = pd.read_sql_query(sql, self.db)
        res = res.to_dict('records')
        return res

    def getHerosPageList(self, curPage:int, pageSize:int):
        sql = f'select * from heros limit {(curPage-1)*pageSize}, {pageSize}'
        res = pd.read_sql_query(sql, self.db)
        res = res.to_dict('records')
        return res


if __name__ == '__main__':
    print(Model().getHeros(2, 5))
