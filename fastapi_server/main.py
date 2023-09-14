from fastapi import FastAPI, Query
import uvicorn
from pydantic import BaseModel
from model import Model
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title='web server')

origins = [
    "http://localhost:3200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/getHerosByName/')
def getHerosByName(name:str):  # Query传默认参数，还可以设置一些别的内容
    return Model().getHerosByName(name)

@app.get('/getHerosByRole/')
def getHerosByRole(role_main:str):  # Query传默认参数，还可以设置一些别的内容
    return Model().getHerosByRole(role_main)


@app.get('/getHerosPageList/')
def getHerosPageList(page: int = Query(1, description='当前页'),
             pageSize: int = Query(10, description='每页数量')):  # Query传默认参数，还可以设置一些别的内容

    return Model().getHerosPageList(page, pageSize)


@app.get('/getRole/')
def get_Role():
    return Model().getHerosRole()


if __name__ == '__main__':
    # reload 热加载，修改了自动重启
    uvicorn.run(app='main:app', reload=True)
