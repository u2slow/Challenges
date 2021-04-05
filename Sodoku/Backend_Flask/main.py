from flask import Flask , request, jsonify
from solve2 import clsolver
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/',methods=['POST'])
def getdata():
    data = request.data
    data = json.loads(data)
    print(data)
    solver = clsolver()
    feld = solver.start(data)
    return jsonify({"message": "get data sucessfully", "Feld": feld})

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "stu"})

if __name__ =="__main__":
    app.run(debug=True)