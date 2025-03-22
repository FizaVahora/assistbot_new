from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200579690"})  

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Extract the intent name
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    if intent_name == "GetWeatherInfo":
        response_text = "The weather is sunny with a temperature of 25°C."
    else:
        response_text = "Sorry, I didn't understand that request."

    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
