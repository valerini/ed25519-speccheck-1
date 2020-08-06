import json

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ed25519

if __name__ == "__main__":
    with open('../cases.json') as f:
        data = json.load(f)
    print('backend version text: ' + default_backend().openssl_version_text())
    print('backend version num: {}'.format(default_backend().openssl_version_number()))
    for i, test_case in enumerate(data):
        try:
            pub_key = ed25519.Ed25519PublicKey.from_public_bytes(bytes.fromhex(test_case['pub_key']))
            msg = bytes.fromhex(test_case['message'])
            sig = bytes.fromhex(test_case['signature'])
            pub_key.verify(sig, msg)
            print('{}: true'.format(i))
        except:
            print('{}: false'.format(i))