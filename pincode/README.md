# Pincode Lookup API

A FastAPI example for looking up one or more pincodes. The data is stored in
memory in `data.py`; there is no database or persistence layer.

> **Demo data:** The current dataset contains three four-digit sample values
> with Dhaka and Chittagong locations. It is not an authoritative Indian
> pincode directory.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup and run

Run these commands from the `pincode` directory:

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
| `GET` | `/` | Returns a welcome message |
| `GET` | `/pincode/{pincode}` | Looks up one pincode |
| `POST` | `/pincode/bulk` | Looks up up to 20 pincodes in one request |

### Single lookup

Pincodes must contain exactly four digits. For example:

```bash
curl http://localhost:8000/pincode/1200
```

The response contains the pincode, city, district, division, and state. An
invalid format returns `400`; a valid pincode absent from the sample data
returns `404`.

### Bulk lookup

Send a JSON object with a `pincodes` array containing between 1 and 20
four-digit strings:

```bash
curl -X POST http://localhost:8000/pincode/bulk \
  -H "Content-Type: application/json" \
  -d '{"pincodes":["1200","9999"]}'
```

The response reports the number found and not found, includes matching
locations in `results`, and lists unmatched values in `missing`. Invalid bulk
input is rejected with `422`.

## API documentation

With the server running, open:

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>