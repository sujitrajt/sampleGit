from flask import Flask,render_template,request
import pyodbc

##connecting to mysql
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:rishi1310.database.windows.net,1433;Database=rishi;Uid=adminrishi;Pwd=13101996@Ri$hi;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=45;;')
cr = conn.cursor()

TNAME = ' '
app = Flask(__name__)

@app.route('/')
def signin():
    global TNAME
    TNAME = ' '
    return render_template("signin.html")

@app.route("/task1", methods=["GET", "POST"])
def task1():
    global TNAME
    if(TNAME==' ' ):        
        formdata = dict(request.form)
        TNAME = formdata['tname']
    return render_template("task1.html")

@app.route("/result1", methods=["GET", "POST"])
def result1():
    global TNAME
    formdata = dict(request.form)
    question = formdata['ques']
    cr.execute("insert into qna(tname, question) values (?, ?)", TNAME, question)
    cr.commit()
    return render_template("result1.html")

@app.route("/task2")
def task2():
    global SNAME
    cr.execute("select TOP 1 question,answer from qna where score IS NULL")
    res = cr.fetchall()
    return render_template("task2.html",data=res)

@app.route("/result2", methods=["GET", "POST"])
def result2():
    global TNAME
    formdata = dict(request.form)
    question = formdata['ques']
    grade_student = int(formdata['grade'])
    cr.execute("update qna set score=? where question=?",grade_student,question)
    cr.commit()
    return render_template("result2.html")



