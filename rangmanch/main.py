from contextlib import asynccontextmanager
from fastapi import FastAPI
from db_config import cretae_tables
from routes.reviews import router as reviews_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform any startup tasks here
    cretae_tables()
    print("Database tables created successfully.")
    yield
    # Perform any shutdown tasks here
    print("Shutting down...")


app = FastAPI(
    title="Rangmanch",
    description="A simple API for Rangmanch",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(reviews_router)


@app.get("/")
def root():
    return {"message": "Welcome to Rangmanch API!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, reload=True)
