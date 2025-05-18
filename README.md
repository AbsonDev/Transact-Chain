# TransactChain

## Overview
TransactChain is a powerful and secure blockchain microservice designed for enterprise-grade transaction recording. Built with FastAPI and Python, it provides a robust platform for creating, validating, and tracking immutable financial transactions. The system implements Proof of Work consensus mechanism, ensuring data integrity and security while maintaining high performance through its RESTful API architecture.

Key features include:
- Real-time transaction processing
- Immutable transaction history
- Secure block mining
- Comprehensive API documentation
- Built-in chain validation
- Transaction traceability
- Enterprise-ready architecture

## Features

- 🔒 Secure transaction recording
- ⛏️ Proof of Work mining system
- 🔗 Immutable blockchain structure
- 📝 RESTful API interface
- 📊 Transaction history tracking
- ✅ Chain validation
- 🚀 FastAPI performance

## Project Structure

```
transactchain/
├── api/
│   └── routes.py         # API endpoints
├── core/
│   ├── block.py         # Block implementation
│   └── blockchain.py    # Blockchain core logic
├── models/
│   └── transaction.py   # Transaction model
├── main.py             # FastAPI application
├── test_blockchain.py  # Test script
└── requirements.txt    # Dependencies
```

## Architecture

### Main Components

1. **API Layer (FastAPI)**
   - REST endpoints
   - Data validation
   - Automatic documentation
   - CORS support
   - Error handling

2. **Blockchain Core**
   - Block management
   - Transaction mining
   - Chain validation
   - Proof of Work implementation
   - Hash calculation

3. **Transaction Layer**
   - Transaction model
   - Business rules validation
   - Data persistence
   - Timestamp management

### API Endpoints

#### 1. Create Transaction
```http
POST /api/v1/transactions/
```
**Payload:**
```json
{
    "sender": "string",
    "receiver": "string",
    "amount": float,
    "description": "string"
}
```
**Response:**
```json
{
    "message": "Transaction added successfully",
    "block_index": integer
}
```

#### 2. Mine Block
```http
POST /api/v1/mine/
```
**Response:**
```json
{
    "message": "New block mined successfully",
    "block": {
        "index": integer,
        "timestamp": float,
        "transactions": array,
        "previous_hash": string,
        "hash": string,
        "nonce": integer
    }
}
```

#### 3. Query Blockchain
```http
GET /api/v1/chain/
```
**Response:**
```json
{
    "chain": array,
    "length": integer
}
```

#### 4. Validate Blockchain
```http
GET /api/v1/valid/
```
**Response:**
```json
{
    "is_valid": boolean
}
```

#### 5. Get Transaction History
```http
GET /api/v1/transactions/{address}
```
**Response:**
```json
{
    "address": string,
    "transactions": array,
    "count": integer
}
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/transactchain.git
cd transactchain
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the service:
```bash
python main.py
```

The service will be available at `http://localhost:8000`

## Testing

1. Run the test script:
```bash
python test_blockchain.py
```

2. Test individual endpoints using curl:
```bash
# Create transaction
curl -X POST http://localhost:8000/api/v1/transactions/ \
  -H "Content-Type: application/json" \
  -d '{"sender":"Alice","receiver":"Bob","amount":10,"description":"Payment"}'

# Mine block
curl -X POST http://localhost:8000/api/v1/mine/

# Get chain
curl http://localhost:8000/api/v1/chain/
```

## Development

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all functions
- Keep functions small and focused

### Adding New Features
1. Create a new branch
2. Implement the feature
3. Add tests
4. Update documentation
5. Submit a pull request

## Security

1. **Data Validation**
   - All input data is validated
   - Data types are checked
   - Business rules are applied
   - Input sanitization

2. **Immutability**
   - Transactions cannot be altered
   - Blocks are linked by hashes
   - Chain is constantly validated
   - Proof of Work protection

3. **Traceability**
   - Timestamp on all transactions
   - Unique hash for each block
   - Complete history available
   - Audit trail

## Integration

1. **Webhooks**
   - Configure webhooks to notify the main system
   - Receive real-time updates
   - Event-based architecture

2. **REST API**
   - Simple HTTP integration
   - JSON support
   - Complete documentation
   - Swagger UI available

3. **Events**
   - Transactions created
   - Blocks mined
   - Validations performed
   - Chain updates

## Monitoring

1. **Available Metrics**
   - Number of transactions
   - Blockchain size
   - Validation status
   - Mining difficulty
   - Response times

2. **Logs**
   - Processed transactions
   - Errors and exceptions
   - System events
   - Performance metrics

## Next Steps

1. **Planned Improvements**
   - Authentication implementation
   - Database persistence
   - Query caching
   - Rate limiting
   - Load balancing

2. **Future Features**
   - Smart contracts
   - Reward system
   - Integration with other blockchains
   - WebSocket support
   - Mobile SDK

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers. 