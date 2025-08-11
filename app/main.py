from fastapi import FastAPI
from routes.agents import router as agents_router
from routes.clients import router as clients_router
from routes.projects import router as projects_router
from routes.comments import router as comments_router
from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(clients_router)
app.include_router(agents_router)
app.include_router(projects_router)
app.include_router(comments_router)


@app.get("/")
async def main():
    return {"status": "it works"}
