from typing import Literal

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    status: Literal["success", "failure"]
    details: str = Field(..., description="Concise summary of the test results")
