# FastAPI Basics

A small FastAPI application for learning the fundamentals of API development.
It includes example endpoints for request inspection, active orders, and
restaurants.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup

From this directory, install the project dependencies:

```bash
uv sync
```

## Run the application

Start the development server with:

```bash
uv run fastapi dev main.py
```

The API is available at <http://localhost:8000>.

You can also run the module directly:

```bash
uv run python main.py
```

## API endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome response |
| `GET` | `/debug/request-info` | Returns details from the incoming request |
| `GET` | `/active/orders` | Returns example active orders |
| `GET` | `/restaurants` | Returns example restaurants |

Interactive API documentation is available at:

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>

The order and restaurant data are currently static examples and are not
connected to a database.
