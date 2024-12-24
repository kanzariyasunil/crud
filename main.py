from flask import Flask,request,json
from database import make_db_call
app = Flask(__name__)



@app.route("/",methods = ["GET"])
def home():
    data = make_db_call(query="SELECT roll, name, bike FROM public.crud",returns=True)
    return str(data)

@app.route("/add",methods = ["POST"])
def add():
    roll = request.form.get("roll")
    name = request.form.get("name")
    bike = request.form.get("bike")

    if roll and name and bike:
        querys = "INSERT INTO public.crud(roll, name, bike) VALUES (%(roll)s, %(name)s, %(bike)s);"
        make_db_call(query=querys,parameter={
            "roll" : roll,
            "name" : name,
            "bike" : bike
        })
    return "data will be added"

@app.route("/update",methods = ["PUT"])
def update():
    name = request.form.get("name")
    bike = request.form.get("bike")
    roll = request.form.get("roll")
    querys = ""

    if name and bike:
        querys = "update public.crud set name = %(name)s,bike = %(bike)s where roll = %(roll)s"
    elif name:
        querys = "update public.crud set name = %(name)s where roll = %(roll)s"
    else:
        querys = "update public.crud set bike = %(bike)s where roll = %(roll)s"
    
    make_db_call(query=querys,parameter={
        "roll" : roll,
        "name" : name,
        "bike" : bike
    })

    return "update sussefully"

@app.route("/delete",methods = ["DELETE"])
def delete():
    querys = "delete from public.crud where roll = %(roll)s"
    try:
        make_db_call(query=querys,parameter={
        "roll":request.form.get("roll")
    })
    except:
        return {"message":"Please enter valid roll no"}

    return "data deleted"


if __name__ == "__main__":
    app.run(debug=True)