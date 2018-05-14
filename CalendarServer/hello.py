from flask import Flask
from flask import request
from flask import jsonify
from flask import request
import api_query
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api/get_events', methods = ['POST'])
def get_messages():
    #print("tiger")
    parsed = request.get_json()
    #print(json.dumps(parsed))
    if parsed["input"][0:8] == "schedule":
        return "3"
        #jsonify(api_query.query(int(parsed["input"][8:9])))
            #{'schedule':['flight', 'class']})
    elif parsed["input"][0:9] == "classTime":
        date = "2018-05-13"
        return jsonify(api_query.classTime(parsed["input"][10:20]))
    return jsonify({'error':'no user found'})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")