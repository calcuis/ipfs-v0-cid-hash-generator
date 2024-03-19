import random
import string

def generate_random_cid():
    # Define the length of the CID excluding the "Qm" prefix
    cid_length = 46
    # Generate random characters for the CID
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=cid_length))
    # Construct the CID with the "Qm" prefix
    cid = "Qm" + random_chars
    return cid

# Generate a random CID
random_cid = generate_random_cid()

print("Random IPFS v0 CID:", random_cid)
