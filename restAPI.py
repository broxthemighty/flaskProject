#restAPI.py
from flask import Flask
import json
from Blockchain import Blockchain #Matt* added import for class Blockchain

app =  Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])

def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})

app.run(debug=True, port=5000)