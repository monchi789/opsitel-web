import uvicorn
from app.shared.infrastructure.database import Base, engine
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from app.bootstrap.router import register_routers

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register API routes
register_routers(app)

# Add pagination support
add_pagination(app)

def start_dev():
    """
    Start the development server.
    """
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
