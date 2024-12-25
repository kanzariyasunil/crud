from flask import Flask,request
from database import make_db_call
app = Flask(__name__)




@app.route('/',methods = ["GET"])
def index():
    return "ok! now go on information url "


@app.route("/information",methods = ["GET"])
def information():
    query = "select * from Persons"
    data = make_db_call(query=query,returns=True)
    try:
        response = [{"id":item[0],
                 "name":item[1],
                 } for item in data]
    except Exception as e:
        return str(e)
    return response

@app.route("/add",methods = ["POST"])
def add():
    roll = request.form.get("PersonID")
    name = request.form.get("FirstName")

    if roll and name :
        querys = "INSERT INTO Persons(PersonID , FirstName) VALUES (%(PersonID)s, %(FirstName)s);"
        make_db_call(query=querys,parameters={
            "PersonID" : roll,
            "FirstName" : name,
            
        })
    return "data will be added"

@app.route("/update",methods = ["PUT"])
def update():
    name = request.form.get("FirstName")
    roll = request.form.get("PersonID")
    querys = ""

    if name:
        querys = "update public.Persons set FirstName = %(FirstName)s where PersonID = %(PersonID)s"
    
    
    make_db_call(query=querys,parameters={
        "PersonID" : roll,
        "FirstName" : name,
        
    })

    return "update sussefully"

@app.route("/delete",methods = ["DELETE"])
def delete():
    querys = "delete from public.Persons where PersonID = %(PersonID)s"
    try:
        make_db_call(
            query=querys,
            parameters={
            "PersonID":request.form.get("PersonID")
    })
    except:
        return {"message":"Please enter valid roll no"}

    return "data deleted"




if __name__ == "__main__":
    app.run(debug=True)
    