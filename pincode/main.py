from fastapi import FastAPI
from exception import (
    PinCodeNotFoundError,
    InvalidPinCodeError,
    pincode_not_found_handler,
    invalid_pincode_handler,
)
from models import LocationResponse, PincodeRequest, BulkRequest, BulkResponse
from data import pincode_data

app = FastAPI(
    title="Pincode API",
    description="API for retrieving information about Indian pincodes.",
    version="1.0.0",
)

# Register custom exception handlers
app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pincode API!"}


@app.get("/pincode/{pincode}", response_model=LocationResponse)
def get_location_by_pincode(pincode: str):

    if len(pincode) != 4 or not pincode.isdigit():
        raise InvalidPinCodeError(pincode, "Pincode must be a 4-digit number")

    if pincode not in pincode_data:
        raise PinCodeNotFoundError(pincode)

    return LocationResponse(**pincode_data[pincode])


@app.post("/pincode/bulk", response_model=BulkResponse)
def get_bulk_location(request: BulkRequest):
    found_results = []
    missing_pincodes = []

    for pincode in request.pincodes:
        if pincode in pincode_data:
            found_results.append(LocationResponse(**pincode_data[pincode]))
        else:
            missing_pincodes.append(pincode)

    return BulkResponse(
        found=len(found_results),
        not_found=len(missing_pincodes),
        results=found_results,
        missing=missing_pincodes,
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, reload=True)
