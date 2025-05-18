import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/v1"

def test_blockchain():
    # 1. Add a transaction
    transaction = {
        "sender": "Alice",
        "receiver": "Bob",
        "amount": 10,
        "description": "Payment for services"
    }
    print("\n1. Adding transaction...")
    response = requests.post(f"{BASE_URL}/transactions/", json=transaction)
    print(f"Response: {response.json()}")

    # 2. Mine a block
    print("\n2. Mining block...")
    response = requests.post(f"{BASE_URL}/mine/")
    print(f"Response: {response.json()}")

    # 3. Check blockchain
    print("\n3. Checking blockchain...")
    response = requests.get(f"{BASE_URL}/chain/")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

    # 4. Check transaction history
    print("\n4. Checking Alice's transaction history...")
    response = requests.get(f"{BASE_URL}/transactions/Alice")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    test_blockchain() 