from pydantic import BaseModel


class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    description: str
    available: bool
    price: float


class MenuResponse(BaseModel):
    status: str = "success"
    count: int
    items: list[MenuItem]
