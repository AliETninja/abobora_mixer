from web3 import Web3
from lista import addrss, keys
import random


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

sender_account = {
    "addrss": "0x80bfF6505c15F4E1453031780ea5c94E3da218E9",
    "key": "4a6284456663a4f0430e1974efa2f8df0b9dc41511c1aa4b5e1662d31ffa9c4d"
}
reciver_account = {
    "addrss": "0x300F8A3A0FA5EE5329475CE2c8e6Bf8DCCEa3077",
    "key": "d4f84f29702923af48d292dc9e588567b04b1fe43c196bc345cb650ff2aa6c3c"
}

number_tx = random.randint(0, len(addrss)-1) ** random.randint(0, len(addrss)-1)

temp_1_addrss = sender_account["addrss"]
temp_1_key = sender_account["key"]
temp = random.randint(0, len(addrss)-1)
temp_2_addrss = addrss[temp]

for i in range(number_tx):

    addrss_1 = temp_1_addrss
    addrss_2 = temp_2_addrss

    private_key = temp_1_key

    nonce = w3.eth.getTransactionCount(addrss_1)

    tx = {
        'nonce': nonce,
        'to': addrss_2,
        'value': w3.toWei(1, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei('50', 'gwei'),
    }

    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(w3.toHex(tx_hash))

    temp_1_addrss = temp_2_addrss
    temp_1_key = keys[temp]

    temp = random.randint(0, len(addrss) - 1)
    temp_2_addrss = addrss[temp]
    if i == number_tx - 1:
        addrss_1 = temp_1_addrss
        addrss_2 = reciver_account["addrss"]

        private_key = temp_1_key

        nonce = w3.eth.getTransactionCount(addrss_1)

        tx = {
            'nonce': nonce,
            'to': addrss_2,
            'value': w3.toWei(1, 'ether'),
            'gas': 21000,
            'gasPrice': w3.toWei('50', 'gwei'),
        }

        signed_tx = w3.eth.account.signTransaction(tx, private_key)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(w3.toHex(tx_hash))

