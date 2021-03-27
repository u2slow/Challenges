from flask import Flask , request, jsonify
import solve

app = Flask(__name__)

@app.route('/',methods=['GET'])
def getdata():
    data = request.data
    solvedFeld = solve.mainLoop()
    return {"message": "get data sucessfully"}

if __name__ =="__main__":
    app.run(debug=True)