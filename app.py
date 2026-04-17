from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({"message": "API is running"}), 200

@app.route('/health')
def health():
    return jsonify({"message": "healthy"}), 200

@app.route('/me')
def me():
    return jsonify({
        "name": "Mobolaji Philip Babajide",
        "email": "mobolaji0babajide@gmail.com",
        "github": "https://github.com/philipswitch"
    }), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)