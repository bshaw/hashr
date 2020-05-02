# hashr

Provides a simple RESTful API for calculating the hash value for a given input.

## Setup

Setup the virtual environment, install dependencies, and start the dev server:

```bash
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
pip install -e .

FLASK_APP=hashr flask run
```

## Usage

Send an HTTP GET request containing the desired hash algorithm and string to hash as arguments:

```bash
$ curl http://127.0.0.1:5000/hash/sha256/foo
{
  "data": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
}

```

You must specify a hash algorithm supported by the Python [hashlib](https://docs.python.org/3/library/hashlib.html) module.
