from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/api/calculate/Area/rectangle")
def calculate_area_of_rectangle():
    width = int(request.args.get('width'))
    height = int(request.args.get('height'))
    Area = width * height

    response = {"width": width, "height": height, "Area": Area}

    return jsonify(response)
