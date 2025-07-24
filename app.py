from flask import Flask, request, render_template_string

app = Flask(__name__)

template = """
<!doctype html>
<html>
<head>
    <title>Nth Largest Finder</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 40px; }
        h2 { color: #2c3e50; }
        input, textarea { width: 300px; padding: 8px; margin-bottom: 10px; }
        button { padding: 8px 16px; }
        .result { margin-top: 20px; font-size: 18px; color: green; }
        .error { margin-top: 20px; font-size: 18px; color: red; }
    </style>
</head>
<body>
    <h2>Nth Largest App is Live!</h2>
    <form method="POST">
        <label>Enter numbers (comma-separated):</label><br>
        <textarea name="numbers" rows="3">{{ request.form.numbers or '' }}</textarea><br>

        <label>Enter n (e.g., 2 for 2nd largest):</label><br>
        <input type="number" name="n" value="{{ request.form.n or '' }}"><br>

        <button type="submit">Find Nth Largest</button>
    </form>

    {% if result %}
        <div class="result">The nth largest number is: {{ result }}</div>
    {% elif error %}
        <div class="error">{{ error }}</div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        try:
            numbers = [float(x.strip()) for x in request.form['numbers'].split(',') if x.strip()]
            n = int(request.form['n'])
            if n <= 0 or n > len(numbers):
                raise ValueError("Invalid value of n.")
            numbers.sort(reverse=True)
            result = numbers[n - 1]
        except Exception as e:
            error = f"Error: {str(e)}"
    return render_template_string(template, result=result, error=error, request=request)

if __name__ == '__main__':
    app.run(debug=True)
