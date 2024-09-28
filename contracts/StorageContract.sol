// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StorageContract {
    struct File {
        string ipfsHash;
        bytes nonce;
        bytes tag;
    }

    mapping(string => File) private files;

    event FileStored(string ipfsHash, bytes nonce, bytes tag);

    // Store file metadata on blockchain
    function storeFile(string memory ipfsHash, bytes memory nonce, bytes memory tag) public {
        files[ipfsHash] = File(ipfsHash, nonce, tag);
        emit FileStored(ipfsHash, nonce, tag);
    }

    // Retrieve file metadata from blockchain
    function getFileMetadata(string memory ipfsHash) public view returns (bytes memory, bytes memory) {
        require(bytes(files[ipfsHash].ipfsHash).length > 0, "File not found");
        File memory file = files[ipfsHash];
        return (file.nonce, file.tag);
    }

    // Check if a file exists
    function fileExists(string memory ipfsHash) public view returns (bool) {
        return bytes(files[ipfsHash].ipfsHash).length > 0;
    }
}
