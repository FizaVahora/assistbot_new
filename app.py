from flask import Flask, request, jsonify
import os 

app = Flask(__name__)

# Route to return student number in JSON format
@app.route('/', methods=['GET'])
def home():
    return jsonify({"student_number": "200579690"})  

# Webhook route must accept POST requests
@app.route('/webhook', methods=['POST'])  
def webhook():
    # Get request JSON
    req = request.get_json(silent=True, force=True)
    
    # Extract intent name
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    # Generate response based on intent
    if intent_name == "GetWeatherInfo":
        response_text = "The weather is sunny with a temperature of 25°C."
    else:
        response_text = "Sorry, I didn't understand that request."

    # Return fulfillment response
    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)

