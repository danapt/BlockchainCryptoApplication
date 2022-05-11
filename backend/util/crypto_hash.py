import hashlib
import json

def crypto_hash(*args):
    """
    return a sha-256 hash of the given arguments:
    """
    stringified_args = sorted(map(lambda data:json.dumps(data), args))
    #print(f"stringified_args:  {stringified_args}")

    joined_data =''.join(stringified_args)
    #print(f"joined_data:  {joined_data}")

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_has('1',2,[3]): {crypto_hash('1',2,[3])}")

    print(f"crypto_has(2,'1', [3]): {crypto_hash(2,'1', [3])}")

if __name__ == '__main__':
    main()