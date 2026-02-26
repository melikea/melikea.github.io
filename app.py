from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Initial data for the table
    return render_template('index.html', initial_multiplier=5)

@app.route('/update_table', methods=['POST'])
def update_table():
    multiplier = int(request.json['multiplier'])
    # Generate new table data based on the slider value
    data = [{"index": i, "value": i * multiplier} for i in range(1, 11)]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
