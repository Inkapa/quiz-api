import databases
import sqlalchemy
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

# Cors configuration (example below allows all)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Used to avoid conflict with Heroku
uri = os.getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

metadata = sqlalchemy.MetaData()
database = databases.Database(uri)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    """
    Connect to the database asynchronously on startup
    """
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """
    Disconnect from the database asynchronously on shutdown
    """
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
