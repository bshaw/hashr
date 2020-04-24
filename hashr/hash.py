import hashlib
from flask import Blueprint, jsonify, request

bp = Blueprint('hash', __name__, url_prefix='/hash')

@bp.route('/<hash_algorithm>/<hash_data>', methods=['GET'])
def caclulate_hash(hash_algorithm, hash_data):
    hash = hashlib.new(hash_algorithm)
    hash.update(hash_data.encode('utf8'))
    return jsonify({'data': hash.hexdigest()})
