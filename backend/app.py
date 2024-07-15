from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/api/predict', methods=['POST'])
def make_prediction():
    data = request.json
    input_data = data.get('input', [])
    if not input_data:
        return jsonify({'error': 'No input data provided'}), 400
    
    result = predict(input_data)
    return jsonify({'predictions': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
