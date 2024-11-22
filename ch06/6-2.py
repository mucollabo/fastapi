from fastapi import FastAPI, Depends, Query

app = FastAPI()

# dependency function
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {'name': name, 'valid': True}

# route function / web endpoint
@app.get('/user')
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user
    