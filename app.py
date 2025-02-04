from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/5ka')
def store1():
    with open('all_products_5ka.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/magnit')
def store2():
    with open('all_products_magnit.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/5ka_cat')
def store3():
    with open('categories_5ka.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/magnit_cat')
def store4():
    with open('categories_magnit.json') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
