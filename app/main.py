from fastapi import FastAPI, Depends, HTTPException, APIRouter

from typing import Any
from sqlalchemy.orm import Session

from app.schemas.todo_entry import TodoEntryCreate, TodoEntryUpdate, TodoEntry
from app import deps
from app import crud


# Initialize the app
app = FastAPI(
    title="Todo List API",
    description="A simple API for managing a todo list",
    openapi_url="/api/v1/openapi.json"
)

# Initialize the router
api_router = APIRouter()


# Define the routes
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


@api_router.get("/entry/{id}", status_code=200, response_model=TodoEntry)
def fetch_todo_entry(
    *,
    id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single to-do entry by id
    """
    result = crud.todo_entry.get(db=db, id=id)
    if not result:
        raise HTTPException(status_code=404,
                            detail=f"Entry not found for id {id}")
    return result


@api_router.post("/entry", status_code=201, response_model=TodoEntry)
def create_entry(
    *,
    entry_in: TodoEntryCreate,
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new to-do entry
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
    """
    entry = crud.todo_entry.get(db=db, id=entry_in.id)
    if not entry:
        raise HTTPException(status_code=404,
                            detail=f"Entry not found for id {entry_in.id}")
    entry = crud.todo_entry.update(db=db, db_obj=entry, obj_in=entry_in)
    return entry


@api_router.delete("/entry/{id}", status_code=200, response_model=TodoEntry)
def delete_entry(
    *,
    id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete an existing to-do entry
    """
    entry = crud.todo_entry.get(db=db, id=id)
    if not entry:
        raise HTTPException(status_code=404,
                            detail=f"Entry not found for key {id}")
    entry = crud.todo_entry.remove(db=db, id=entry.id)
    return entry


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002, log_level="info")
