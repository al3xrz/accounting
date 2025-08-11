from fastapi import FastAPI
from routes.agents import router as agents_router
from routes.clients import router as clients_router
from routes.projects import router as projects_router
from routes.comments import router as comments_router
from routes.expenses import router as expenses_router
from routes.fields import router as fields_router
from routes.investor import router as investors_router
from routes.playground import router as playground_router
from routes.status import router as statuses_router
from routes.tc import router as tc_router
from routes.ttype import router as ttype_router

from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(clients_router)
app.include_router(agents_router)
app.include_router(projects_router)
app.include_router(comments_router)
app.include_router(expenses_router)
app.include_router(fields_router)
app.include_router(investors_router)
app.include_router(playground_router)
app.include_router(statuses_router)
app.include_router(tc_router)
app.include_router(ttype_router)

@app.get("/")
async def main():
    return {"status": "it works"}
