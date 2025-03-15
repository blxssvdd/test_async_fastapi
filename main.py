from fastapi import FastAPI, Query
import uvicorn

import data


app = FastAPI()
users = []


@app.get("/")
async def index():
    return dict(msg="Вітаємо в нашій інформаційній системі")



@app.get("/get_users/")
def get_users():
    return {"users": users}



@app.post("/add_user/")
async def add_user(name: str = Query(description="Введіть своє ім'я")):
     if name not in data.db:
        users.append(name)
        return dict(msg="Дані додано.")



@app.delete("/del_user/")
def del_user(name: str = Query(description="Введіть ім'я для видалення")):
    if name not in users:
        return dict(msg="Немає такого ім'я")
    users.remove(name)
    return dict(msg="Ім'я видалено.")



if __name__ == "__main__":
    uvicorn.run("main:app")