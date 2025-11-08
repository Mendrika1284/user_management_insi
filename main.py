from fastapi import FastAPI

app = FastAPI()

users = [{"id": 1, "nom": "Andry", "age": 23},
         {"id": 2, "nom": "Koto", "age": 40},
         {"id": 3, "nom": "Sarah", "age": 20},
]

@app.get('/users')
def get_all_users():
    return {"data": users, "msg": "displayed successfully", "code": 200}