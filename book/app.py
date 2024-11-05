from flask import Flask, jsonify

app = Flask(__name__)

# Sample book data
books = [
    {"id": 1, "title": "Book One", "author": "Author One", "available": True},
    {"id": 2, "title": "Book Two", "author": "Author Two", "available": False},
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
