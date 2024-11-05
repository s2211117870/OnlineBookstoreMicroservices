from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users[data['username']] = data['password']
    return jsonify({'message': 'User registered!'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
