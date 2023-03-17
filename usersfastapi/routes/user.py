from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get("/users")
async def get_users():
    result = conn.execute(users.select()).fetchall()
    keys = ['id', 'name', 'email', 'password']
    arreglo = []
    for x in result:
        usuario = dict(zip(keys, x))
        arreglo.append(usuario)
    print(arreglo)
    return arreglo


@user.post("/users")
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    keys = ['id', 'name', 'email', 'password']
    print(dict(zip(keys, conn.execute(users.select().where(
        users.c.id == result.lastrowid)).first())))
    return dict(zip(keys, conn.execute(users.select().where(
        users.c.id == result.lastrowid)).first()))


@user.get("/users/{id}")
def get_user(id: str):
    keys = ['id', 'name', 'email', 'password']
    return dict(zip(keys, conn.execute(users.select().where(users.c.id == id)).first()))


@user.delete("/users/{id}")
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return "Eliminado"


@user.put("/users/{id}")
def update_user(id: str, user: User):
    new_user = {"id": id, "name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.update().where(
        users.c.id == id).values(new_user))
    conn.commit()
    keys = ['id', 'name', 'email', 'password']
    return dict(zip(keys, conn.execute(users.select().where(
        users.c.id == id)).first()))
