# hashr

Provides a simple RESTful API for calculating the hash value for a given input.

## Usage

Send an HTTP GET request containing the desired hash algorithm and string to hash as arguments:

```bash
$ curl http://127.0.0.1:5000/hash/sha256/foo
{
  "data": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
}

```

You must specify a hash algorithm supported by the Python [hashlib](https://docs.python.org/3/library/hashlib.html) module.
