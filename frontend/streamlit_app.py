import streamlit as st
from backend.ipfs_client import upload_file
from backend.encryption import encrypt_file, decrypt_file
from backend.blockchain import store_metadata, get_file_metadata
from Crypto.Random import get_random_bytes

st.title("Decentralized Cloud Storage System")

# Simple test in streamlit_app.py
if st.button('Test IPFS Connection'):
    file_bytes = b'Hello, IPFS!'  # Sample data for testing
    ipfs_hash = upload_file(file_bytes)
    st.write(f"IPFS Hash: {ipfs_hash}")


# Upload File
st.subheader("Upload and Encrypt File")
uploaded_file = st.file_uploader("Choose a file")
encryption_key = st.text_input("Enter a 16-byte encryption key", max_chars=16)

if uploaded_file and encryption_key:
    file_bytes = uploaded_file.read()

    # Encrypt the file
    key = encryption_key.encode()
    ciphertext, nonce, tag = encrypt_file(file_bytes, key)

    # Upload encrypted file to IPFS
    ipfs_hash = upload_file(ciphertext)
    st.write(f"File uploaded to IPFS with hash: {ipfs_hash}")

    # Store metadata on blockchain
    tx_hash = store_metadata(ipfs_hash, nonce, tag)
    st.write(f"Metadata stored on blockchain with transaction hash: {tx_hash.hex()}")

# Retrieve File
st.subheader("Retrieve and Decrypt File")
ipfs_hash_input = st.text_input("Enter IPFS hash of file")
decryption_key = st.text_input("Enter decryption key for the file", max_chars=16)

if ipfs_hash_input and decryption_key:
    # Retrieve file from IPFS
    encrypted_file = upload_file.cat(ipfs_hash_input)

    # Retrieve metadata from blockchain
    nonce, tag = get_file_metadata(ipfs_hash_input)

    # Decrypt file
    key = decryption_key.encode()
    try:
        decrypted_file = decrypt_file(encrypted_file, key, nonce, tag)
        st.write("File successfully decrypted!")
        st.download_button("Download Decrypted File", decrypted_file, file_name="decrypted_file")
    except ValueError:
        st.write("Incorrect decryption key or corrupted data.")
