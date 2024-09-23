from typing import Dict, Optional

from pydantic import BaseModel

from enum import Enum


class ErrorCode(int, Enum):
    others = 0


class ErrorResponse(BaseModel):
    error: str
    code: Optional[ErrorCode] = None


class ErrorWithDataResponse(ErrorResponse):
    data: Dict
