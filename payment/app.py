from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample payment data
payments = []

@app.route('/pay', methods=['POST'])
def process_payment():
    data = request.json
    payment = {
        "payment_id": len(payments) + 1,
        "order_id": data.get("order_id"),
        "amount": data.get("amount"),
        "status": "completed"
    }
    payments.append(payment)
    return jsonify({"message": "Payment processed!", "payment": payment}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
