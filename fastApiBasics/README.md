# FastAPI Basics

A small FastAPI learning project with sample endpoints for inspecting requests
and browsing example orders and restaurants.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup

Run these commands from the `fastApiBasics` directory:

```bash
uv sync
uv run fastapi dev main.py
```

The API starts at <http://localhost:8000>. Alternatively, run it directly:

```bash
uv run python main.py
```

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns `{"Hello": "World"}` |
| `GET` | `/debug/request-info` | Returns request method, URL, headers, parameters, and client host |
| `GET` | `/active/orders` | Returns a sample list of active orders |
| `GET` | `/restaurants` | Returns a sample list of restaurants |

The orders and restaurants are hard-coded examples; no database is configured.
The request-inspection endpoint includes request headers in its response, so
use it for local learning rather than exposing it publicly.

## API documentation

With the server running, open:

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>
