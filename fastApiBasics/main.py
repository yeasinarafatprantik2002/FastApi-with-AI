from fastapi import FastAPI, Request

app = FastAPI(
    title="FastAPI Basics",
    description="This is a simple FastAPI application that demonstrates the basics of building an API using FastAPI. It includes endpoints for basic CRUD operations and serves as a starting point for building more complex applications",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/debug/request-info")
async def request_info(request: Request):
    """ "Inspect the raw request object and return its details."""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
        "client": request.client.host if request.client else None,
    }


@app.get(
    "/active/orders",
    summary="Get active orders",
    description="Retrieve a list of active orders from the database.",
    tags=["Orders"],
    response_description="A list of active orders with their details.",
    deprecated=False,
)
def get_active_orders():
    """Get active orders from the database."""
    # Placeholder for database query logic
    active_orders = [
        {"order_id": 1, "item": "Masala Dosa", "status": "active"},
        {"order_id": 2, "item": "Idli Sambar", "status": "out_for_delivery"},
        {"order_id": 3, "item": "Vada Pav", "status": "active"},
    ]
    return {"active_orders": active_orders}


@app.get(
    "/restaurants",
    summary="Get restaurants",
    description="Retrieve a list of restaurants from the database.",
    tags=["Restaurants"],
    response_description="A list of restaurants with their details.",
    deprecated=False,
)
def get_restaurants():
    """Get restaurants from the database."""
    # Placeholder for database query logic
    restaurants = [
        {"restaurant_id": 1, "name": "Dosa Corner", "cuisine": "South Indian"},
        {"restaurant_id": 2, "name": "Sambar House", "cuisine": "South Indian"},
        {"restaurant_id": 3, "name": "Vada Pav Express", "cuisine": "Street Food"},
    ]
    return {"restaurants": restaurants}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, reload=True)
