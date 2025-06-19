# resources/message.py
from flask import Blueprint, jsonify, request

# Create a Blueprint for message-related routes
message_bp = Blueprint('message', __name__)

messages = []

@message_bp.route('/messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})

@message_bp.route('/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400
    messages.append(data['message'])
    return jsonify({"message": "Message added!"}), 201
