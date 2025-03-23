from flask import Flask, request, jsonify

app = Flask(__name__)

# Route 1: Return student number (for testing)
@app.route('/student-info', methods=['GET'])
def student_info():
    return jsonify({"student_number": "123456789"})  # Replace with your student number

# Route 2: Handle Dialogflow Webhook for "Place Order"
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    # Extract intent name
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    # Define a response
    response_text = "I couldn't understand that request."

    if intent_name == "Place Order":
        response_text = "Your order request has been received! What would you like to order?"

    # Send response back to Dialogflow
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)