#!/usr/bin/python3
import os
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
##postgress
engine = create_engine("mysql+pymysql://root:azad123@localhost:3306/sohail")


db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=['GET'])
def index():
      
    return render_template("index.html")


@app.route("/add_student", methods=['GET'])
def insert_new_student():
    return render_template("insert_new_student.html")
    

@app.route("/intro", methods=['POST', 'GET'])
def intro():
    if request.method == "POST":

        First_Name = request.form.get("First_Name")
        Last_Name = request.form.get("Last_Name")
        Session = request.form.get("Session")
        Due_fee = request.form.get("Due_fee")
        Submitted = request.form.get("Submitted")
        Total_fee = request.form.get("Total_fee")
        db.execute("INSERT into Fee(First_Name, Last_Name, Session, Due_fee, Submitted, Total_fee) VALUES (:First_Name, :Last_Name, :Session, :Due_fee, :Submitted, :Total_fee)",
                {"First_Name": First_Name, "Last_Name": Last_Name, "Session":Session, "Due_fee": Due_fee, "Submitted": Submitted, "Total_fee": Total_fee})
        db.commit()

        # Get all records again
        students = db.execute("SELECT * FROM Fee").fetchall()
        return render_template("intro.html", students=students)
    else:
        students = db.execute("SELECT * FROM Fee").fetchall()
        return render_template("intro.html", students=students)





if __name__ == "__main__":
    app.run(debug=True)