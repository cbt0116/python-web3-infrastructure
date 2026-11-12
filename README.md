# Python Web3 Infrastructure

A lightweight Python utility module for connecting to EVM-compatible JSON-RPC endpoints, validating and normalizing wallet addresses, and retrieving basic network information.

This is a portfolio prototype focused on reusable Web3 setup helpers using `web3.py`.

## Features

The current implementation in `web3_utils.py` provides three functions:

| Function | Purpose |
|---|---|
| `make_web3(rpc_url=None)` | Creates a Web3 HTTP provider using an explicit URL or the `RPC_URL` environment variable, then checks connectivity |
| `normalize_address(address)` | Validates an EVM address and returns its checksum format |
| `chain_summary(w3)` | Returns the connected chain ID, current block number, and client version |

The HTTP provider is configured with a 15-second request timeout.

## Tech stack

- Python 3.11+
- web3.py
- pytest

## Requirements

- Python 3.11 or newer
- An HTTP JSON-RPC endpoint for an EVM-compatible network when using `make_web3`

## Installation

Clone the repository:

```bash
git clone https://github.com/cbt0116/python-web3-infrastructure.git
cd python-web3-infrastructure
```

Create and activate a virtual environment.

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Set an RPC endpoint in your environment. Do not commit private endpoints containing credentials.

**Windows PowerShell**
```powershell
$env:RPC_URL="https://your-rpc-endpoint"
```

**macOS / Linux**
```bash
export RPC_URL="https://your-rpc-endpoint"
```

## Usage

Connect to a network and print a basic summary:

```python
from web3_utils import make_web3, chain_summary

w3 = make_web3()
print(chain_summary(w3))
```

You can also pass an RPC URL directly:

```python
from web3_utils import make_web3

w3 = make_web3("https://your-rpc-endpoint")
print("Connected:", w3.is_connected())
```

Validate and checksum-format an address:

```python
from web3_utils import normalize_address

wallet = normalize_address("0x0000000000000000000000000000000000000000")
print(wallet)
```

The zero address above is used only as a formatting example; it is not a valid user wallet for transactions.

## Tests

Run the current pytest suite:

```bash
pytest
```

The existing test checks that `normalize_address` raises `ValueError` for an invalid address string. Additional tests should cover valid address normalization, missing RPC configuration, connection failures, and `chain_summary` using a mocked Web3 instance.

## Current scope and limitations

- The module provides connection, address-formatting, and network-summary helpers.
- It does not currently implement contract-call wrappers, transaction signing, or transaction submission.
- The connection check requires a reachable RPC endpoint.
- No private keys or seed phrases are required by the current implementation.
- The project is a prototype, not a production financial service or audited infrastructure library.

## Potential improvements

- Add unit tests for all helper functions with mocked providers
- Add configurable request timeouts
- Add typed return models and clearer error types
- Add optional read-only contract-call helpers with ABI validation
- Add CI for linting and tests across supported Python versions

## Security

Never commit private keys, seed phrases, API credentials, or RPC URLs containing secrets. Use environment variables or a dedicated secrets manager for sensitive configuration. Review dependencies and behavior before using this code in a production environment.

## License

No repository-level LICENSE file is currently documented. Add one to clarify reuse and distribution terms.
