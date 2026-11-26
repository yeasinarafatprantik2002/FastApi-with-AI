from pydantic import BaseModel, field_validator


class PincodeRequest(BaseModel):
    pincode: str

    # pincode must be a 4-digit number
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 4 or not value.isdigit():
            raise ValueError("Pincode must be a 4-digit number")

        return value


class LocationResponse(BaseModel):
    pincode: str
    city: str
    district: str
    division: str
    state: str


class BulkRequest(BaseModel):
    pincodes: list[str]

    # Validate each pincode in the list
    @field_validator("pincodes", mode="before")
    @classmethod
    def validate_bulk_pincodes(cls, value):
        if len(value) == 0:
            raise ValueError("Pincodes list cannot be empty")

        if len(value) > 20:
            raise ValueError("Cannot request more than 20 pincodes at once")

        for pincode in value:
            if len(pincode) != 4 or not pincode.isdigit():
                raise ValueError(f"Invalid pincode format: {pincode}")
        return value


class BulkResponse(BaseModel):
    success: str = "success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]
