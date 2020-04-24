from flask import Flask, jsonify, request
import hashlib

app = Flask(__name__)


@app.route('/hash/<hash_algorithm>/<hash_data>', methods=['GET'])
def caclulate_hash(hash_algorithm, hash_data):
    hash = hashlib.new(hash_algorithm)
    hash.update(hash_data.encode('utf8'))
    return jsonify({'data': hash.hexdigest()})


if __name__ == '__main__':
    app.run(debug=True)
