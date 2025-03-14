from fastapi import FastAPI, Query
import uvicorn

from data import db


app = FastAPI()


@app.get("/")
async def index():
    return dict(msg="Вітаємо в нашій інформаційній системі")


@app.post("/add_user/")
async def add_user(name: str = Query(description="Введіть своє ім'я"), age: int = Query(None, description="Введіть свій вік")):
    if name in db:
        return dict(msg="Користувач з таким іменем існує")

    db.update({name: age})
    return dict(msg="Дані успішно оновлено")


@app.get("/users/")
async def get_users():
    return dict(msg="Запит дозволено", users=db)


@app.get("/user/")
async def get_user(name: str = Query(description="Введіть ім'я для пошуку")):
    if not name in db:
        return dict(msg="Такого користувача не знайдено")

    return dict(msg=f"Користувач з іменем {name} має вік {db[name]}")


if __name__ == "__main__":
    uvicorn.run("main:app")

