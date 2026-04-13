from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/image', methods=["GET", "POST"])
def image_skill():
    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleImage": {
                    "imageUrl": "https://i.ifh.cc/NqhMQ1.jpg",
                    "altText": "tfscrdd"
                }
            }]
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

