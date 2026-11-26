from fastapi.responses import JSONResponse
from fastapi import Request


class PinCodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode


class InvalidPinCodeError(Exception):
    def __init__(self, pincode: str, reason: str = "Invalid pincode format"):
        self.pincode = pincode
        self.reason = reason


# Custom exception handler for PinCodeNotFoundError
async def pincode_not_found_handler(request: Request, exc: Exception):
    if not isinstance(exc, PinCodeNotFoundError):
        raise TypeError("Expected PinCodeNotFoundError")

    return JSONResponse(
        status_code=404,
        content={
            "error": "Pincode not found",
            "message": f"The pincode '{exc.pincode}' does not exist in our records.",
            "pincode": exc.pincode,
        },
    )


# Custom exception handler for InvalidPinCodeError
async def invalid_pincode_handler(request: Request, exc: Exception):
    if not isinstance(exc, InvalidPinCodeError):
        raise TypeError("Expected InvalidPinCodeError")

    return JSONResponse(
        status_code=400,
        content={
            "error": "Invalid pincode",
            "message": exc.reason,
            "pincode": exc.pincode,
        },
    )
