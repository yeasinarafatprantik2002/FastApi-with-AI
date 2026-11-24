# Chai Menu API

A small FastAPI project that serves a sample menu of chai, snacks, and combos.
Menu entries are stored as in-memory data in `data.py`; no database or
persistence is configured.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup and run

Run these commands from the `chaimenu` directory:

```bash
uv sync
uv run fastapi dev main.py
```

The API starts at <http://localhost:8000>. To run the application directly:

```bash
uv run python main.py
```

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome message |
| `GET` | `/menu` | Returns all menu items |
| `GET` | `/menu?category=chai` | Filters menu items by category |
| `GET` | `/menu/{item_id}` | Returns a menu item by its numeric ID |

Category matching is case-insensitive. A category with no matching items
returns `404`; an unknown menu item ID also returns `404`. Each menu item
includes its ID, name, category, description, availability, and price.

## API documentation

With the server running, open:

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>