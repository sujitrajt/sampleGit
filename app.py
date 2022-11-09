# NAME : SUJITRAJ THIRUMURTHY
# UTA ID : 1001830297


#References 
#LINKS : 
# 1) https://absolutecodeworks.com/python-flask-crud-sample-with-sql-server
# 2) https://thewebdev.info/2022/04/03/how-to-display-image-on-a-html-page-with-python-flask
# 3) https://www.youtube.com/watch?v=9MHYHgh4jYc&ab_channel=TechWithTim
# 4) https://www.youtube.com/watch?v=3hllGdiM2Ys&ab_channel=EvilProgrammer
# 5) https://tomlogs.github.io/build-a-photos-application-with-azure-blob-storage   
# 6) https://stackoverflow.com/questions/34262872/how-to-find-user-location-within-500-meters-from-given-lat-and-long-in-python
# 7) https://stackoverflow.com/questions/10207193/sql-select-the-last-3-dates-from-a-table
# 8) https://docs.microsoft.com/en-us/sql/t-sql/functions/dateadd-transact-sql?view=sql-server-ver16
# 9) https://www.w3schools.com/css/css_table.asp (css styling of tables)
# 10) https://www.sqlservertutorial.net/sql-server-basics/sql-server-update-join/
# 11) nltk.org/api/nltk.tokenize.html
# 12) https://www.nltk.org/index.html
# from fileinput import filename
# from cmath import cos, sin, sqrt

# IMPORT LIBRARIES 



from collections import Counter
from flask import Flask, flash, redirect, render_template, request, url_for
import pyodbc
import os
import sqlite3
import re
from turbo_flask import Turbo

#INSTANTIATING APP
app = Flask(__name__)
turbo = Turbo(app)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

if __name__ == '__main__':
    # app.run(debug=True,port=8084)
    app.run()

