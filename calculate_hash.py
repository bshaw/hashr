import sys
import hashlib

hash_data = sys.argv[1]
hash_algorithm = sys.argv[2]


def caclulate_hash(hash_data, hash_algorithm):
    hash = hashlib.new(hash_algorithm)
    hash.update(hash_data.encode('utf8'))
    return hash.hexdigest()


print(caclulate_hash(hash_data, hash_algorithm))
