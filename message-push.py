from nacl.public import PrivateKey, PublicKey, SealedBox
# Playing with crypto, simple push to file receiver.
import requests
import base64
def main():
    #key_gen()
    o = auth()
    print(o)

def key_gen():
    key = PrivateKey.generate()
    encoded_public_key = key.public_key.encode(encoder=nacl.encoding.Base64Encoder)
    encoded_private_key = key.encode(encoder=nacl.encoding.Base64Encoder)

    # loaded_public_key = PublicKey(encoded_public_key, encoder=nacl.encoding.Base64Encoder)
    # assert loaded_public_key.encode() == key.public_key.encode()

    with open('private_key', 'wb') as f:
	#f.write('Hello\n')
        f.write(encoded_private_key)
    with open('public_key', 'wb') as f:
        f.write(encoded_public_key)

def auth():
    auth_host = '10.50.8.128' 
    #with open('private_key', 'rb') as f:
        #f.write('Hello\n')
    with open('private_key') as f: encoded_private_key = f.read()
    with open('public_key') as f: encoded_public_key = f.read()
    loaded_public_key = PublicKey(encoded_public_key, encoder=nacl.encoding.Base64Encoder)
    loaded_private_key = PrivateKey(encoded_private_key, encoder=nacl.encoding.Base64Encoder)
    # assert loaded_public_key.encode() == loaded_private_key.public_key.encode()
    #assert loaded_public_key.encode() == loaded_private_key.public_key.encode()
    print(loaded_public_key.encode())
    print(loaded_private_key.public_key.encode())
    private_key = loaded_private_key
    public_key = loaded_public_key

    # return 1

    # private_key = private_key_b64.decode('base64')
    # public_key = public_key_b64.decode('base64')

    # with open('public_key', 'rb') as f:
    #     f.write(encoded_public_key)
    # with open('x.py') as f: s = f.read()
    # # Generate Bob's private key, as we've done in the Box example
    # skbob = PrivateKey.generate()
    # pkbob = skbob.public_key
    #return private_key 

    # Alice wishes to send a encrypted message to Bob,
    # but prefers the message to be untraceable
    #sealed_box = SealedBox(pkbob)
    sealed_box = SealedBox(private_key)

    # This is Alice's message
    message = b"Kill all kittens"

    # Encrypt the message, it will carry the ephemeral key public part
    # to let Bob decrypt it
    encrypted = sealed_box.encrypt(message)
    msg = base64.b64encode(encrypted)
    msg = encoded_public_key
    #data = {'name': 'jtest', 'ipaddr': '192.168.0.2' 'public_key': b'\x8e\x05{\xe2\xcby:\x0b\xeb\xe69\xac|\x96\xff\xa4\xdaE\x89^\xa7\xaf\x90\x83\x14)bP\x0c\n\x85l'}
    #data = {'msg': ''}
    data = {'msg': msg}
    print(data)
    #return 1
    #r = requests.post('https://stats.rchain.me:30443/auth', data = data)
    r = requests.post(f'https://{auth_host}:30443/auth', data = data)
    print(r)
    text = r.text
    content = r.content
    print(text)
    print(content)


if __name__ == '__main__':
    main()
