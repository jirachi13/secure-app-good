from flask import Flask, jsonify, request
import re

app = Flask(__name__)


def is_valid_username(username: str) -> bool:
    """Allow only alphanumeric usernames between 3 and 20 characters."""
    return bool(re.match(r'^[a-zA-Z0-9]{3,20}$', username))


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200


@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json(silent=True)
    if not data or 'username' not in data:
        return jsonify({"error": "Missing 'username' field"}), 400

    username = data['username']

    if not isinstance(username, str) or not is_valid_username(username):
        return jsonify({"error": "Invalid username"}), 422

    return jsonify({"message": f"Hello, {username}!"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
