from fastapi import FastAPI

from app.routers import accounts, categories

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "ok"}


app.include_router(accounts.router)
app.include_router(categories.router)
