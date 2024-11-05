from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample order data
orders = []

@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    order = {
        "order_id": len(orders) + 1,
        "user": data.get("user"),
        "book_id": data.get("book_id"),
        "quantity": data.get("quantity"),
        "status": "pending"
    }
    orders.append(order)
    return jsonify({"message": "Order created!", "order": order}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
