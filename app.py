from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Nth Largest App is Live!"

@app.route('/nth-largest', methods=['POST'])
def nth_largest():
    data = request.get_json()
    numbers = data['numbers']
    n = data['n']
    if not numbers or n > len(numbers) or n <= 0:
        return jsonify({"error": "Invalid input"}), 400
    numbers.sort(reverse=True)
    return jsonify({"nth_largest_number": numbers[n - 1]})
