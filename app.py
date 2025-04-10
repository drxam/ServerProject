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

@app.route('/okey')
def store3():
    with open('all_products_okey.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/perekrestok')
def store4():
    with open('all_products_perekrestok.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/5ka_cat')
def store5():
    with open('categories_5ka.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/magnit_cat')
def store6():
    with open('categories_magnit.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/okey_cat')
def store7():
    with open('categories_okey.json') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/perekrestok_cat')
def store8():
    with open('categories_perekrestok.json') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
