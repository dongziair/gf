from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/electric/predict', methods=['POST'])
def get_fixed_value():
    data = request.json
    return jsonify({'value': 5})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
