

from typing import Any
from fastapi import HTTPException, status
from app.schemas.response import StandardResponse


class APIException(HTTPException):

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        data: Any = None,
    ):
        response_data = StandardResponse(success=False, message=message, data=data)
        super().__init__(status_code=status_code, detail=response_data.dict())
