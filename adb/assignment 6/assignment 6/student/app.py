from flask import Flask,render_template,request
from turbo_flask import Turbo
import pyodbc
import threading
import time
import datetime

##connecting to mysql
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:rishi1310.database.windows.net,1433;Database=rishi;Uid=adminrishi;Pwd=13101996@Ri$hi;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=45;;')
cr = conn.cursor()

SNAME = ' '
app = Flask(__name__)
turbo = Turbo(app)

@app.route('/')
def signin():
    return render_template("signin.html")

@app.route("/task1", methods=["GET", "POST"])
def task1():
    global SNAME
    if(SNAME==' ' ):        
        formdata = dict(request.form)
        SNAME = formdata['sname']
    cr.execute("select TOP 1 question,hint from qna where answer IS NULL")
    res = cr.fetchall()
    return render_template("task1.html",data=res)


@app.route("/result1", methods=["GET", "POST"])
def result1():
    formdata = dict(request.form)
    question = formdata['ques']
    answer = formdata['ans']
    cr.execute("update qna set answer=?,sname=? where question=?",answer,SNAME,question)
    cr.commit()
    return render_template("result1.html")

@app.route('/task2')
def task2():
    global SNAME
    cr.execute("select TOP 1 question, answer, score from qna where sname like ?",SNAME)
    res1 = cr.fetchall()
    score_list = list()
    for i in res1:
        if(i[2]!=True):
            score_list.append(0)
        else:
            score_list.append(i[2])     
    cumulative1 = sum(score_list)
    avger = cumulative1/len(score_list)
    return render_template("task2.html",data=res1, avg = avger, cum = cumulative1)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

