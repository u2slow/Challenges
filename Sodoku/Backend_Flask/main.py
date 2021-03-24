from flask import Flask , request, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def solve():
    data = request.data
    print(data)
    return {"message": "good morning"}

if __name__ =="__main__":
    app.run(debug=True)