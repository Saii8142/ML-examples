from flask import Flask, request, jsonify

app = Flask(__name__)

# List to store messages
messages = []

@app.route('/', methods=['GET'])
def home():
    return "Hello, my name is Kiran"

@app.route('/messages', methods=['POST'])
def post_message():
    # Correct way to get JSON data from the request
    data = request.get_json()

    # Check if 'message' exists in the JSON data
    message = data.get('message') if data else None

    if message:
        # Append the message to the list
        messages.append(message)
        return jsonify({"message": messages[-1]}), 201  # Respond with status 201 for created
    
    return jsonify({"error": "No message provided"}), 400  # Respond with status 400 for bad request

if __name__ == '__main__':
    app.run(debug=True)
