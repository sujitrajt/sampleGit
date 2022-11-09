from flask import Flask,render_template,request
from turbo_flask import Turbo
import pyodbc

##connecting to mysql
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:rishi1310.database.windows.net,1433;Database=rishi;Uid=adminrishi;Pwd=13101996@Ri$hi;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=45;;')
cr = conn.cursor()

app = Flask(__name__)
turbo = Turbo(app)

@app.route("/", methods=["GET", "POST"])
def task1():
    cr.execute("select * from qna")
    res1 = cr.fetchall()
    data_list=list()
    for r in res1:
        print(r[5])
        if (r[5]==None):
            data_list.append(r)
    print(data_list)
    return render_template("task1.html",data=res1, data1=data_list)


@app.route("/result1", methods=["GET", "POST"])
def result1():
    formdata = dict(request.form)
    question = formdata['ques']
    print(question)
    hint = formdata['hint']
    cr.execute("update qna set hint=? where question like ?",hint,question)
    cr.commit()
    return render_template("result1.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

