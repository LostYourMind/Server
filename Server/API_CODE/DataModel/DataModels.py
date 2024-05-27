from pydantic import BaseModel
from typing import List, Dict, Optional


class Message(BaseModel):
    text: str
    sender: str
    id_Value: int
    paymentData: Optional[dict] = None


# 결제 응답 데이터 모델
class PaymentResponse(BaseModel):
    message: str
    success: bool
    total_amount: int = 0


class PaymentRequest(BaseModel):
    user_id: int
    action: str
    paymentData: dict = None


class AddToCartRequest(BaseModel):
    user_id: int
    items: List[str]