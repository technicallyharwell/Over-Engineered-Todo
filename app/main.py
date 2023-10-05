from fastapi import FastAPI, Depends, APIRouter

from sqlalchemy.orm import Session

from app.schemas.todo_entry import TodoEntry
from app import deps
from app import crud
from app.routers import todoentries

# Initialize the app
app = FastAPI(
    title="Todo List API",
    description="A simple API for managing a todo list",
    openapi_url="/api/v1/openapi.json"
)
app.include_router(todoentries.router, prefix="/api/v1")

# Initialize the root route
api_router = APIRouter()


@app.on_event("startup")
def startup_event() -> None:
    """
    Startup event, called when the app starts up
    :return:
    """
    from app.postgres_pre_start import init_db
    init_db()


# Define the root route
@api_router.get("/", status_code=200, response_model=dict[str, list[TodoEntry]])
def root(
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Root endpoint, returns a list of first 5 to-do entries

    :return:
    """
    entries = crud.todo_entry.get_multi(db, skip=0, limit=5)
    return {"entries": entries}


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002, log_level="info")
