# Import the necessary libraries
import web3
import os

# Set the number of addresses to generate
num_addresses = 10

# Set the file to save the keys to
filename = "keys.txt"

# Set up the Web3 object and connect to the Ethereum network
w3 = web3.Web3(web3.Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR-API-KEY"))

# Generate the addresses and private keys
addresses = []
private_keys = []
for i in range(num_addresses):
    # Generate a new account
    account = w3.eth.account.create()

    # Add the address and private key to the lists
    addresses.append(account.address)
    private_keys.append(account.privateKey.hex())

# Write the keys to the file
with open(filename, "w") as f:
    for i in range(num_addresses):
        f.write("Address: " + addresses[i] + "\n")
        f.write("Private key: " + private_keys[i] + "\n")
        f.write("\n")

# Print the addresses and private keys
print("Addresses:", addresses)
print("Private keys:", private_keys)

