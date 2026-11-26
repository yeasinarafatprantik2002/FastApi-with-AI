# FastAPI Learning Projects

This repository contains three independent FastAPI examples:

| Project | Description |
| --- | --- |
| [`fastApiBasics`](./fastApiBasics/README.md) | Request inspection and sample order and restaurant endpoints |
| [`chaimenu`](./chaimenu/README.md) | An in-memory chai, snack, and combo menu API |
| [`pincode`](./pincode/README.md) | Single and bulk lookups against an in-memory pincode dataset |

Each project has its own `pyproject.toml`, `uv.lock`, and virtual environment.
Run commands from the project's directory; dependencies are not managed from
the repository root.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

## Quick start

For example, to run the pincode API:

```bash
cd pincode
uv sync
uv run fastapi dev main.py
```

The other projects use the same commands from their respective directories.
Each app listens on `http://localhost:8000` by default, so run only one at a
time unless you configure different ports.

When an app is running, its interactive API documentation is available at
[`/docs`](http://localhost:8000/docs) and its ReDoc documentation at
[`/redoc`](http://localhost:8000/redoc).
