##
import pandas as pd
from sklearn.linear_model import LinearRegression

"""
df = pd.read_csv("D:/NTU/AI with Advanced Predictive Techniques in Finance/3/FoodExpenditure(1).csv")
Y = df.loc[:,["foodexp"]]
X = df.loc[:,["income"]]
model = LinearRegression()
model.fit(X,Y)
pred = model.predict(X)
from sklearn.metrics import mean_squared_error
rmse = mean_squared_error(Y,pred)**0.5
"""
##
from flask import Flask, request, render_template
import sqlite3
import datetime
from markupsafe import Markup
app = Flask(__name__)
name_flag = 0
name = ""
@app.route("/",methods=['GET','POST'])
#app.route is a decorator
def index():
    return (render_template("index.html"))

@app.route("/main",methods=['GET','POST'])
def main():
    global name_flag, name
    if name_flag == 0:
        name = request.form.get("name")
        name_flag = 1
        conn = sqlite3.connect("log.db")
        c = conn.cursor()
        timestamp = datetime.datetime.now()
        c.execute("insert into employee(name,timestamp) values (?,?)", (name, timestamp))
        conn.commit()
        c.close()
        conn.close()
    return (render_template("main.html",name=name))

@app.route("/ethical_test",methods=['GET','POST'])
def ethical_test():
    #if request
    return (render_template("ethical_test.html"))

@app.route("/query",methods=['GET','POST'])
def query():
    conn = sqlite3.connect("log.db")
    c = conn.execute("select * from employee")
    r = ""
    for row in c:
        r = r+str(row)+"<br>"
    print(r)
    r = Markup(r)
    c.close()
    conn.close()
    return (render_template("query.html",r=r))

@app.route("/answer",methods=['GET','POST'])
def result():
    ans = request.form["options"]
    #print(ans)
    if ans == "TRUE":
        return (render_template("true.html"))
    else:
        return (render_template("false.html"))

@app.route("/foodexp",methods=['GET','POST'])
def foodexp():
    return (render_template("foodexp.html"))

@app.route("/prediction",methods=['GET','POST'])
def prediction():
    income = float(request.form.get("income"))
    return (render_template("prediction.html", r=(income*0.485)*147))

@app.route("/delete",methods=['GET','POST'])
def delete():
    conn = sqlite3.connect("log.db")
    c = conn.cursor()
    #timestamp = datetime.datetime.now()
    c.execute("delete from employee")
    conn.commit()
    c.close()
    conn.close()
    return (render_template("delete.html"))



@app.route("/end",methods=['GET','POST'])
def end():
    return (render_template("end.html"))


if __name__ == "__main__":
    app.run()