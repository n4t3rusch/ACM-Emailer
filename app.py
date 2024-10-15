from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello')
def hello():
       return jsonify(message="Hello from Flask!")

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.json['data']
    # Process the data here. For this example, we'll just reverse the string.
    processed_data = data[::-1]
    return jsonify(message=f"I reversed the string!(in backend): {processed_data}")


if __name__ == '__main__':
       app.run(debug=True)