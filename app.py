from flask import Flask,jsonify,request
app = Flask(__name__)
data = [
    {
        "id":1,
        "contact":u"12345678",
        "name":u"Raju",
        "done":False,
    },
    {
        "id":2,
        "contact":u"87654321",
        "name":u"Rahul",
        "done":False,
    }
]
@app.route("/")
def Hello_World():
    return "Hi how are you?"
@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error", 
            "message":"Please Provide the Data",
        },400)
    task = {
        "id":data[-1]["id"]+1,
        "contact":request.json["contact"],
        "name":request.json.get("name",""),
        "done":False
    }
    data.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": data
    })

if __name__ == "__main__":
    app.run(debug = True)