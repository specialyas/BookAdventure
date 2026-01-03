

from typing import Any
from fastapi import status
from app.schemas.response import StandardResponse
from app.utils.exceptions import APIException


def bad_request_response(message: str, data: Any = None) -> APIException:
    return APIException(message, status.HTTP_400_BAD_REQUEST, data)

def success_response(message: str, data: Any = None) -> StandardResponse:
    return StandardResponse(success=True, message=message, data=data)

def not_found_response(resource: str) -> StandardResponse:
    return StandardResponse(success=False, message=f"{resource} not found", data=None)
