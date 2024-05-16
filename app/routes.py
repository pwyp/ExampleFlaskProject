from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Returns a JSON response with a 'message' key set to 'Hello, World!'.
    """
    return jsonify(message='Hello, World!')

@app.route('/analyze_message', methods=['POST'])
def analyze_message():
    """
    Analyzes the message received from the request and returns the word count.

    Returns:
        A JSON response containing the word count of the message.
    """
    data = request.get_json()
    message = data.get('message', '')
    word_count = len(message.split())
    return jsonify(word_count=word_count)

if __name__ == '__main__':
    app.run()