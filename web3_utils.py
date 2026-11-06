import os
from web3 import Web3

def make_web3(rpc_url=None):
    url = rpc_url or os.getenv("RPC_URL")
    if not url:
        raise ValueError("RPC_URL is required")
    w3 = Web3(Web3.HTTPProvider(url, request_kwargs={"timeout": 15}))
    if not w3.is_connected():
        raise ConnectionError("Unable to connect to EVM RPC")
    return w3

def normalize_address(address: str) -> str:
    if not Web3.is_address(address):
        raise ValueError("Invalid EVM address")
    return Web3.to_checksum_address(address)

def chain_summary(w3):
    return {
        "chain_id": w3.eth.chain_id,
        "block_number": w3.eth.block_number,
        "client": w3.client_version
    }
