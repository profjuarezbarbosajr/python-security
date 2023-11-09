# pycoin 

from pycoin.networks.registry import network_for_netcode
network = network_for_netcode("BTC")

from pycoin.symbols.btc import network

key = network.keys.private(secret_exponent=1)  # this is a terrible key because it's very guessable
print(key.wif())
print(key.sec())
print(key.address())
print(key.address(is_compressed=False))

key = network.keys.bip32_seed(b"foo")  # this is a terrible key because it's very guessable
print(key.hwif(as_private=1))
print(key.hwif())
print(key.wif())
print(key.sec())
print(key.address())

key = network.parse.bip32("xprv9s21ZrQH143K31AgNK5pyVvW23gHnkBq2wh5aEk6g1s496M"
      "8ZMjxncCKZKgb5jZoY5eSJMJ2Vbyvi2hbmQnCuHBujZ2WXGTux1X2k9Krdtq")
print(key.hwif(as_private=1))
print(key.hwif())
print(key.wif())
print(key.sec())
print(key.address())
