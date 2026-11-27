from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])


class LiveResponse(BaseModel):
    status: Literal["ok"] = "ok"


@router.get("/live")
def live() -> LiveResponse:
    """프로세스 생존 여부 확인 (외부 의존성 검사 없음)."""
    return LiveResponse()
