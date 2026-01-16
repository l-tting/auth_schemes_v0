from fastapi import FastAPI

import models, database

app = FastAPI()


models.Base.metadata.create_all(database.engine)

@app.get('/')
def test():
   return "Test success"

@app.post('/register')
def register_user():
   pass
