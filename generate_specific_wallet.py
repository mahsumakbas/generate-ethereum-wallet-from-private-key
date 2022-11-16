import ecdsa
from Crypto.Hash import keccak

random_number_for_private_key = 31334737451456268050498185842994455999554006395290392504114029053954839148697
private_key_hex = hex(random_number_for_private_key)[2:]
print("It is your private key and keep in secret(Never share to anyone/anywhere): \n" + str(private_key_hex))

private_key_bytes = bytes.fromhex(private_key_hex)
private_key_object=ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)

public_key = private_key_object.get_verifying_key().to_string()
public_key_hex = private_key_object.get_verifying_key().to_string().hex()
print("It is public key. No problem to share: \n"+str(public_key_hex))

public_key_as_bytes = bytes.fromhex(str(public_key_hex))
keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(public_key_as_bytes)
full_keccak_hash= str(keccak_hash.hexdigest())

wallet_address = full_keccak_hash[24:]
print("Your public wallet address: 0x"+ wallet_address)

