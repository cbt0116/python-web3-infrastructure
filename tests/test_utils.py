import pytest
from web3_utils import normalize_address

def test_rejects_invalid_address():
    with pytest.raises(ValueError):
        normalize_address("not-an-address")
