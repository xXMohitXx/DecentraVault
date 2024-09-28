import requests

class IPFSClient:
    def __init__(self):
        self.api_address = "http://127.0.0.1:5001/api/v0"  # IPFS API address

    def add_file(self, file_path):
        with open(file_path, 'rb') as file:
            response = requests.post(f"{self.api_address}/add", files={'file': file})
            return response.json()  # Returns IPFS hash

    def store_file_metadata(self, ipfs_hash, nonce, tag):
        # Add your smart contract interaction code here
        pass

    def add_and_store_file(self, file_path, nonce, tag):
        result = self.add_file(file_path)
        ipfs_hash = result.get('Hash')  # Get the IPFS hash
        self.store_file_metadata(ipfs_hash, nonce, tag)  # Store metadata
