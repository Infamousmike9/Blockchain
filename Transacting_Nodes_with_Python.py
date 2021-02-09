
from web3 import Web3
from eth_account import Account
from pathlib import Path
from getpass import getpass



#Connect web3 to MyCRypto:
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

#Look at latest block:
latest_block = w3.eth.blockNumber
print(latest_block)

#balance for node1 from address when creating node copied to notepad:
balance_node1 = w3.eth.getBalance("0x0daf09b88cA3CbF31059653D4DA6b998beBb7f63")
print(balance_node1)

private_key = "0x686048bd0170706121e17b3bd771d69b75ed34906924186ee044ada771f7bd11"

my_account = Account.from_key(private_key) 
print(my_account.address)

def create_raw_txn(account, amount, recipient):
    gas_estimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )


    return{
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas":gas_estimate,
        "nonce": w3.eth.getTransactionCount(account.address)
    }

def send_txn(account, amount, recipient):
    txn = create_raw_txn(account, amount, recipient)
    signed_txn = account.sign_transaction(txn)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return result.hex()

#Send ether to newly created wallet:
#Recipient is wallet you created
result = send_txn(my_account, 9999999999999999999999999999, "0xc5E262E8F01965ee7c4D22cf93E398b1C81D62E8")
print(result) 