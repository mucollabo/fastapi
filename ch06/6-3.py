from fastapi import FastAPI, Depends, Query

app = FastAPI()

# dependency function
def check_dep(name: str = Query(...), gender: str = Query(...)):
    if not name:
        raise

# route function / web endpoint
@app.get('/check_user', dependencies=[Depends(check_dep)])
def get_user() -> bool:
    return True
    