from fastapi import FastAPI, Depends, HTTPException, APIRouter

from typing import Any
from sqlalchemy.orm import Session
from pathlib import Path

from app.schemas.todo_entry import TodoEntryCreate, TodoEntryUpdate, TodoEntry
from app import deps
from app import crud

# Directories
ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent

# Initialize the app
app = FastAPI(
    title="Todo List API",
    description="A simple API for managing a todo list",
    openapi_url="/api/v1/openapi.json"
)

# Initialize the router
api_router = APIRouter()


# Fail the quality gate check
def fail_quality_gate():
    arg1 = 1
    arg2 = 2
    return arg1 + arg2


# Define the routes
@api_router.get("/", status_code=200)
def root(
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Root endpoint, returns a list of first 5 to-do entries

    :return:
    """
    some_num = fail_quality_gate()
    print(f"some_num: {some_num}", flush=True)
    entries = crud.todo_entry.get_multi(db, skip=0, limit=5)
    return {"success": True, "entries": entries}


@api_router.get("/entry/{entry_key}", status_code=200, response_model=TodoEntry)
def fetch_todo_entry(
    *,
    entry_key: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single to-do entry by keyword

    :return:
    """
    result = crud.todo_entry.get(db=db, key=entry_key)
    if not result:
        raise HTTPException(status_code=404,
                            detail=f"Entry not found for key {entry_key}")
    return result


@api_router.post("/entry", status_code=201, response_model=TodoEntry)
def create_entry(
    *,
    entry_in: TodoEntryCreate,
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new to-do entry

    :return:
    """
    entry = crud.todo_entry.create(db=db, obj_in=entry_in)
    return entry


@api_router.put("/entry", status_code=200, response_model=TodoEntry)
def update_entry(
    *,
    entry_in: TodoEntryUpdate,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Update an existing to-do entry

    :return:
    """
    entry = crud.todo_entry.get(db=db, key=entry_in.key)
    print(f"entry: {entry} for PUT", flush=True)
    if not entry:
        raise HTTPException(status_code=404,
                            detail=f"Entry not found for key {entry_in.key}")
    entry = crud.todo_entry.update(db=db, db_obj=entry, obj_in=entry_in)
    return entry


@api_router.delete("/entry/{entry_key}", status_code=200, response_model=TodoEntry)
def delete_entry(
    *,
    entry_key: str,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete an existing to-do entry

    :return:
    """
    entry = crud.todo_entry.get(db=db, key=entry_key)
    if not entry:
        raise HTTPException(status_code=404,
                            detail=f"Entry not found for key {entry_key}")
    entry = crud.todo_entry.remove(db=db, id=entry.id)
    return entry


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
