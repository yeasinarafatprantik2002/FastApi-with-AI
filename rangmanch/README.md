# Rangmanch Review API

A FastAPI application for storing and managing reviews of plays. Reviews are
stored in a local SQLite database using SQLModel. The database tables are
created when the application starts.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Setup and run

Run these commands from the `rangmanch` directory:

```bash
uv sync
uv run fastapi dev main.py
```

The API starts at <http://localhost:8000>. To run the application directly:

```bash
uv run python main.py
```

The SQLite database is `rangmanch.db` in the current working directory.

## Review fields

- `play_name` (string): name of the play
- `reviewer_name` (string): name of the reviewer
- `rating` (integer): required, from 1 through 5
- `comment` (string or `null`): optional

The API assigns each review an ID and creation timestamp.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome message |
| `POST` | `/review/` | Creates a review |
| `GET` | `/review/` | Lists reviews, optionally filtered and paginated |
| `GET` | `/review/average/{play_name}` | Returns a play's average rating and review count |
| `GET` | `/review/{review_id}` | Retrieves a review by ID |
| `PATCH` | `/review/{review_id}` | Updates a review's rating and/or comment |
| `DELETE` | `/review/{review_id}` | Deletes a review |

### Create a review

```bash
curl -X POST http://localhost:8000/review/ \
  -H "Content-Type: application/json" \
  -d '{
    "play_name": "Hamlet",
    "reviewer_name": "A. Reviewer",
    "rating": 5,
    "comment": "A memorable performance."
  }'
```

The rating must be between 1 and 5. Invalid request data returns `422`.

### List and filter reviews

`GET /review/` accepts:

- `play_name`: exact play-name filter
- `skip`: number of rows to skip; defaults to `0`
- `limit`: maximum rows to return; defaults to `10` and must be from `1` to `50`

For example:

```bash
curl "http://localhost:8000/review/?play_name=Hamlet&skip=0&limit=10"
```

### Average rating

For example, `GET /review/average/Hamlet` returns:

```json
{
  "play_name": "Hamlet",
  "average_rating": 4.5,
  "review_count": 2
}
```

The average is rounded to two decimal places. A play with no reviews returns
`404`. Retrieving, updating, or deleting a review ID that does not exist also
returns `404`.

## API documentation

With the server running, open:

- Swagger UI: <http://localhost:8000/docs>
- ReDoc: <http://localhost:8000/redoc>