from typing import List, Dict, Any, Optional
from time import time
from core.block import Block
from models.transaction import Transaction

class Blockchain:
    """Blockchain class following the Liskov Substitution Principle"""
    
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.pending_transactions: List[Dict[str, Any]] = []
        self.difficulty = difficulty

    def create_genesis_block(self) -> Block:
        """Creates the genesis block"""
        return Block(0, [], time(), "0")

    def get_latest_block(self) -> Block:
        """Returns the latest block in the chain"""
        return self.chain[-1]

    def add_transaction(self, transaction: Transaction) -> int:
        """Adds a new transaction"""
        transaction.timestamp = time()
        self.pending_transactions.append(transaction.dict())
        return len(self.chain)

    def mine_pending_transactions(self) -> Block:
        """Mines pending transactions"""
        if not self.pending_transactions:
            raise ValueError("No pending transactions")

        new_block = Block(
            len(self.chain),
            self.pending_transactions,
            time(),
            self.get_latest_block().hash
        )
        
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def get_chain(self) -> List[Dict[str, Any]]:
        """Returns the entire chain in dictionary format"""
        return [block.to_dict() for block in self.chain]

    def is_chain_valid(self) -> bool:
        """Validates the chain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def get_block_by_index(self, index: int) -> Optional[Block]:
        """Returns a block by index"""
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None

    def get_transaction_history(self, address: str) -> List[Dict[str, Any]]:
        """Returns the transaction history for an address"""
        history = []
        for block in self.chain:
            for transaction in block.transactions:
                if transaction["sender"] == address or transaction["receiver"] == address:
                    history.append(transaction)
        return history 