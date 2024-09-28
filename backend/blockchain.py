from web3 import Web3
import json

# Connect to local Ethereum node (Ganache)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Load the contract ABI and contract address
with open('build/contracts/StorageContract.json') as f:
    contract_data = json.load(f)
    contract_abi = contract_data['abi']

contract_address = 'your_deployed_contract_address_here'
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def store_metadata(ipfs_hash, nonce, tag):
    """Stores file metadata (IPFS hash, nonce, tag) on the blockchain."""
    tx_hash = contract.functions.storeFile(ipfs_hash, nonce, tag).transact({'from': w3.eth.accounts[0]})
    w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_hash

def get_file_metadata(ipfs_hash):
    """Fetches file metadata (nonce, tag) from the blockchain."""
    return contract.functions.getFileMetadata(ipfs_hash).call()
