from fastapi import FastAPI, APIRouter, Query

from data.schemas import ToDoEntry, ToDoEntryCreate

app = FastAPI(title="Interview Todo Application", openapi_url="/openapi.json")
api_router = APIRouter()

TODO_LIST = []

# TODO - add delete method, validations and exception handling for duplicate entries, ...
# TODO - tests, containerize, ...

@api_router.get("/todos", status_code=200)
def fetch_todo_list() -> list:
    """
    Fetch the entire todo list; no pagination, no maxsize
    :return:
    """

    return TODO_LIST


@api_router.get("/todo/{key}", status_code=200, response_model=ToDoEntry)
def fetch_todo_entry(*, key: str) -> dict:
    """
    Fetch a single todo entry from the list
    :param key:
    :return:
    """
    entry = [item for item in TODO_LIST if item["key"] == key]
    if entry:
        return entry[0]


@api_router.post("/todo", status_code=201, response_model=ToDoEntry)
def create_new_entry(*, new_item: ToDoEntryCreate) -> ToDoEntry:
    """
    Create a new ToDo entry and add it to the todo list
    :param new_item:
    :return:
    """
    # do not add duplicate key to list
    entry = [item for item in TODO_LIST if item["key"] == new_item.key]
    if entry:
        # raise 403/405/etc
        # TODO - research best practices for this use case
        pass
    new_entry_id = len(TODO_LIST) + 1
    new_entry = ToDoEntry(
        id=new_entry_id,
        key=new_item.key
    )
    TODO_LIST.append(new_entry.model_dump())
    print(TODO_LIST, flush=True)
    return new_entry


@api_router.put("/todo", status_code=200, response_model=ToDoEntry)
def update_entry(*, update_item: ToDoEntryCreate) -> ToDoEntry:
    """
    Update an existing todo entry by toggling is_complete to True
    :param update_item:
    :return:
    """
    entry = [item for item in TODO_LIST if item["key"] == update_item.key]
    if entry:
        entry[0]["is_complete"] = True
    print(TODO_LIST, flush=True)
    return entry[0]


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
