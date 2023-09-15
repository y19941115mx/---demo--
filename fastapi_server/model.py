import pandas as pd
from sqlalchemy import create_engine
from math import ceil

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
        data = pd.read_sql_query(sql, self.db)
        data = data.to_dict('records')

        res = {}
        res["data"] = data
        res["total"] = len(data)
        return res

    def getHerosRole(self):
        # 执行sql语句
        sql = r'select distinct role_main as `key`, role_main as `label` from heros;'
        res = pd.read_sql_query(sql, self.db)
        res = res.to_dict('records')
        return res

    def getHerosByRole(self, role_main:str):
        sql = f'select * from heros where role_main = "{role_main}"'
        df_data = pd.read_sql_query(sql, self.db)
        data = df_data.to_dict('records')
        
        res = {}
        res["data"] = data
        res["total"] = len(data)
        return res

    def getHerosPageList(self, curPage:int, pageSize:int):
        sql = r"select count(*) as num from heros"
        df_data = pd.read_sql_query(sql, self.db)
        total = df_data.loc[0, "num"]

        sql = f'select * from heros limit {(curPage-1)*pageSize}, {pageSize}'
        df_data = pd.read_sql_query(sql, self.db)
        data = df_data.to_dict('records')
        
        res = {}
        res["data"] = data
        res["total"] = int(total)
        res["pageCount"] = ceil(int(total) / pageSize)
        return res


if __name__ == '__main__':
    print(Model().getHerosPageList(1, 5))
