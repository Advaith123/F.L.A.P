from flask import Flask, jsonify
import Getting_data as d
# from flask_jsonify import jsonify
app = Flask(__name__)

@app.route('/home')
def home():
    return d.final_df.to_json()


@app.route('/')
def plswork():
    return "<h1>Hello World!!!!!!!!!!!!!!!!!!!!!!!!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
