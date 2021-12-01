from flask import Flask, render_template, request, jsonify, g
import time
from app import app


@app.route('/')
def home():
    return render_template('form.html')

@app.route('/handle',methods=['GET'])
def handle():
    mean = calculate_mean(str(request.args["seq"]))
    mean_result = {
        "mean": mean
    }
    return jsonify(mean_result)

def calculate_mean(seq: str):
    values = seq.split(";")
    try:
        float_values = [float(x) for x in values]
        mean = sum(float_values) / len(float_values)
        return round(mean, 2)
    except Exception:
        return "error parsing in floats."

# times
@app.before_request
def before_request():
    g.start = time.time()

@app.after_request
def after_request(response):
    diff = time.time() - g.start
    g.request_time = diff
    return response

#if __name__ == '__main__':
#    app.run(host="0.0.0.0", port="5000", debug=True)

