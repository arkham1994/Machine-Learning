from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_home_price', methods=["POST"])
def predict_home_price():
    sqft = int(request.form['sqft'])
    bath = float(request.form['bath'])
    bhk = float(request.form['bhk'])
    rank = int(request.form['rank'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(sqft, bath, bhk, rank)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print('Starting Python Flask server for Bengaluru House Prediction...')
    util.load_saved_artifacts()
    app.run(debug=True)
