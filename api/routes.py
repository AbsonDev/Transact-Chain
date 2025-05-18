from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from core.blockchain import Blockchain
from models.transaction import Transaction

router = APIRouter()
blockchain = Blockchain()

@router.post("/transactions/", response_model=Dict[str, Any])
async def create_transaction(transaction: Transaction) -> Dict[str, Any]:
    """Creates a new transaction in the blockchain"""
    try:
        block_index = blockchain.add_transaction(transaction)
        return {
            "message": "Transaction added successfully",
            "block_index": block_index
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/mine/", response_model=Dict[str, Any])
async def mine_block() -> Dict[str, Any]:
    """Mines a new block with pending transactions"""
    try:
        new_block = blockchain.mine_pending_transactions()
        return {
            "message": "New block mined successfully",
            "block": new_block.to_dict()
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/chain/", response_model=Dict[str, Any])
async def get_chain() -> Dict[str, Any]:
    """Returns the entire blockchain"""
    return {
        "chain": blockchain.get_chain(),
        "length": len(blockchain.chain)
    }

@router.get("/valid/", response_model=Dict[str, bool])
async def validate_chain() -> Dict[str, bool]:
    """Validates the blockchain"""
    return {
        "is_valid": blockchain.is_chain_valid()
    }

@router.get("/transactions/{address}", response_model=Dict[str, Any])
async def get_transaction_history(address: str) -> Dict[str, Any]:
    """Returns the transaction history for an address"""
    history = blockchain.get_transaction_history(address)
    return {
        "address": address,
        "transactions": history,
        "count": len(history)
    } 