# Chai Menu API

A small FastAPI project serving sample chai, snack, and combo menu items.
Entries are held in memory in `data.py`; there is no database or persistence.

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
| `GET` | `/menu/{item_id}` | Returns a menu item by its integer ID |

Category matching is case-insensitive. Categories currently include `chai`,
`snack`, and `combo`. Each item includes its ID, name, category, description,
availability, and price. An unknown category or item ID returns `404`.

## API documentation

With the server running, open:

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>