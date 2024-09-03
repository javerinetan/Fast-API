from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data':{'name':'Javerine'}}

@app.get('/about') #about page 
def about():
    return {'data':'about page'}