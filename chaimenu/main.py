from fastapi import FastAPI, Query, HTTPException

from data import menu_items
from models import MenuItem, MenuResponse

app = FastAPI(
    title="Chai Menu API",
    description="API for managing Chai Menu items",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Chai Menu API!"}


@app.get(
    "/menu",
    response_model=MenuResponse,
    summary="Get the menu items",
    description="Retrieve a list of menu items available in the Chai Menu.",
)
def get_menu(
    category: str | None = Query(None, description="Filter menu items by category")
):

    if category:
        filtered_items = [
            item for item in menu_items if item["category"] == category.lower()
        ]
        if not filtered_items:
            raise HTTPException(
                status_code=404,
                detail="No menu items found for the specified category.",
            )
        return MenuResponse(
            count=len(filtered_items),
            items=[MenuItem(**item) for item in filtered_items],
        )
    return MenuResponse(
        count=len(menu_items),
        items=[MenuItem(**item) for item in menu_items],
    )


@app.get(
    "/menu/{item_id}",
    response_model=MenuItem,
    summary="Get a menu item by ID",
    description="Retrieve a specific menu item by its ID.",
)
def get_menu_item(item_id: int):
    item = next((item for item in menu_items if item["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found.")
    return MenuItem(**item)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, reload=True)
