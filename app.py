from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nth Largest Number App is Live!'

@app.route('/nth-largest', methods=['POST'])
def nth_largest():
    data = request.get_json()
    numbers = data.get('numbers')
    n = data.get('n')

    if not numbers or n <= 0 or n > len(numbers):
        return jsonify({"message": "Invalid input!"}), 400

    # Sort the numbers in descending order and pick the nth largest
    sorted_numbers = sorted(numbers, reverse=True)
    nth_largest_number = sorted_numbers[n - 1]

    return jsonify({"nth_largest_number": nth_largest_number})

if __name__ == '__main__':
    app.run(debug=True)
