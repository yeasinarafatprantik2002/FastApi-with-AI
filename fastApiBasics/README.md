# FastAPI Basics

A small FastAPI learning project demonstrating basic routes, request
inspection, and sample order and restaurant responses. All example data is
hard-coded; there is no database or persistence layer.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup and run

Run these commands from the `fastApiBasics` directory:

```bash
uv sync
uv run fastapi dev main.py
```

The API starts at <http://localhost:8000>. Alternatively, run the application
directly:

```bash
uv run python main.py
```

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns `{"Hello": "World"}` |
| `GET` | `/debug/request-info` | Returns request method, URL, headers, path and query parameters, and client host |
| `GET` | `/active/orders` | Returns sample orders and their statuses |
| `GET` | `/restaurants` | Returns sample restaurant names and cuisines |

`/debug/request-info` includes request headers in its response. Use this
learning endpoint only in a local or trusted environment; do not expose it
publicly.

## API documentation

With the server running, open:

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>
