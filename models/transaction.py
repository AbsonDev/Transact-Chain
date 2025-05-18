from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    """Transaction model following the Single Responsibility Principle"""
    sender: str = Field(..., description="Sender identifier")
    receiver: str = Field(..., description="Receiver identifier")
    amount: float = Field(..., gt=0, description="Transaction amount")
    description: str = Field(..., description="Transaction description")
    timestamp: Optional[float] = Field(default=None, description="Transaction timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "sender": "company_123",
                "receiver": "client_456",
                "amount": 1500.00,
                "description": "Invoice payment #12345"
            }
        } 