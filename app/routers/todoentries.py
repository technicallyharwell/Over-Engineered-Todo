from fastapi import APIRouter, Depends, HTTPException
from typing import Any

from sqlalchemy.orm import Session

from app.schemas.todo_entry import TodoEntryCreate, TodoEntryUpdate, TodoEntry
from app import crud
from app import deps

router = APIRouter(
    prefix="/entries",
)


@router.get("/{id}", status_code=200, response_model=TodoEntry)
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


@router.post("/", status_code=201, response_model=TodoEntry)
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


@router.put("/", status_code=200, response_model=TodoEntry)
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


@router.delete("/{id}", status_code=200, response_model=TodoEntry)
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
