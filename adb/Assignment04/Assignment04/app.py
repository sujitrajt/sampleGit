
from flask import Flask, render_template, request
import pyodbc


app = Flask(__name__)


driver = '{ODBC Driver 17 for SQL Server}'
server = 'rishi1310.database.windows.net'
database = 'rishi'
username = 'adminrishi'
password = '13101996@Ri$hi'

with pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        temp = []
        cursor.execute("SELECT TOP 3 time, id FROM all_month")
        while True:
            r = cursor.fetchone()
            if not r:
                break
            print(str(r[0]) + " " + str(r[1]))
            temp.append(r)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/Task2', methods=['POST', 'GET'])
def ShowPieChart():
    if request.method == 'POST':
            mag1 = request.form['mag1']
            mag2 = request.form['mag2']
            sql = "SELECT count(*) FROM all_month WHERE mag between {} and {}".format(mag1,mag2)
            cursor.execute(sql)
            data = cursor.fetchmany()
            f1 =data[0][0]
            sql1 = "SELECT count(*) FROM all_month WHERE mag <=1"
            cursor.execute(sql1)
            data = cursor.fetchmany()
            f2 = data[0][0]
            print(f2)
            sql2 = "SELECT count(*) FROM all_month WHERE mag between 0 and 1"
            cursor.execute(sql2)
            data = cursor.fetchall()
            f3 =data[0][0]
            print(f3)
            sql3 = "SELECT count(*) FROM all_month WHERE mag between 1 and 2"
            cursor.execute(sql3)
            data = cursor.fetchall()
            f4 =data[0][0]
            sql3 = "SELECT count(*) FROM all_month WHERE mag between 2 and 3"
            cursor.execute(sql3)
            data = cursor.fetchall()
            f5 =data[0][0]
            sql4 = "SELECT count(*) FROM all_month WHERE mag between 3 and 4"
            cursor.execute(sql4)
            data = cursor.fetchall()
            f6 =data[0][0]
            sql5 = "SELECT count(*) FROM all_month WHERE mag between 4 and 5"
            cursor.execute(sql5)
            data = cursor.fetchall()
            f7 =data[0][0]
            return render_template('Task2.html',msg="done", f1 =f1, f2 =f2, f3=f3, f4=f4, f5=f5,f6=f6,f7=f7)

    if request.method == 'GET':
            return render_template('Task2.html')

    else:
        return render_template('index.html')

@app.route('/Task3', methods=['POST', 'GET'])
def ShowBarChart():
    if request.method == 'POST':
            magi1 = request.form['mag1']
            magi2 = request.form['mag2']
            q = "SELECT count(*) FROM all_month WHERE mag between {} and {}".format(magi1,magi2)
            cursor.execute(q)
            data = cursor.fetchmany()
            qf1 =data[0][0]
            q1 = "SELECT count(*) FROM all_month WHERE mag <=1"
            cursor.execute(q1)
            data = cursor.fetchmany()
            qf2 = data[0][0]
            q2 = "SELECT count(*) FROM all_month WHERE mag between 0 and 1"
            cursor.execute(q2)
            data = cursor.fetchall()
            qf3 =data[0][0]
            print(qf3)
            q3 = "SELECT count(*) FROM all_month WHERE mag between 1 and 2"
            cursor.execute(q3)
            data = cursor.fetchall()
            qf4 =data[0][0]
            q4 = "SELECT count(*) FROM all_month WHERE mag between 2 and 3"
            cursor.execute(q4)
            data = cursor.fetchall()
            qf5 =data[0][0]
            q5 = "SELECT count(*) FROM all_month WHERE mag between 3 and 4"
            cursor.execute(q5)
            data = cursor.fetchall()
            qf6 =data[0][0]
            q6 = "SELECT count(*) FROM all_month WHERE mag between 4 and 5"
            cursor.execute(q6)
            data = cursor.fetchall()
            qf7 =data[0][0]
            return render_template('Task3.html',msg="done", f1 =qf1, f2 =qf2, f3=qf3, f4=qf4, f5=qf5,f6=qf6,f7=qf7)

    if request.method == 'GET':
            return render_template('Task3.html')
    else:
        return render_template('index.html')

@app.route('/Task4', methods=['POST','GET'])
def ShowScatterPlot():

        sct1 = "select top 100 mag, all_month.depth from all_month order by time desc"
        cursor.execute(sct1)
        r1 = cursor.fetchall();
        print(r1)
        return render_template('Task4.html', msg="done",r=r1)

@app.route('/Task5', methods=['POST', 'GET'])
def line_chart():
    if request.method == 'POST':
        magWeek1 = request.form['magWeek1']
        magWeek2 = request.form['magWeek2']
        day1 = request.form['d1']
        day2 = request.form['d2']
        sq1 = "SELECT  count(mag) , substring(time, 1, 10) as date from all_month where mag between {} and {} and substring(time, 1, 10) between '{}' and '{}' group by substring(time, 1, 10) order by substring(time, 1, 10)".format(magWeek1 , magWeek2 , day1 , day2)
        cursor.execute(sq1)
        r=cursor.fetchall()
        return render_template('Task5.html', r=r,msg="done")
    if request.method == 'GET':
        return render_template('Task5.html', result="")


if __name__ == '__main__':
    app.run(debug=True,port=5001)
    #app.run(host="0.0.0.0", port=5000)

