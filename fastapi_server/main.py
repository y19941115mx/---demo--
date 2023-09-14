from fastapi import FastAPI, Query
import uvicorn
from pydantic import BaseModel
from model import Model
app = FastAPI(title='web server')


# class BaseItem(BaseModel):
#     网站首页地址: str = None
#     网站名称: str = None


# @app.post('/postdata')
# def get_data(item: BaseItem):
#     return Model().post(item.limit)


@app.get('/getdata/')
def get_data(curpage: int = Query(1, description='当前页'),
             pagesize: int = Query(10, description='每页数量')):  # Query传默认参数，还可以设置一些别的内容

    return Model().getHerosPageList(curpage, pagesize)


if __name__ == '__main__':
    # reload 热加载，修改了自动重启
    uvicorn.run(app='main:app', reload=True)
