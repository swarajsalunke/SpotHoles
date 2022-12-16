from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from geopy.geocoders import Nominatim
import pyodbc

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'tracker'

conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=tcp:locationserver1.database.windows.net,1433;'
                      'DATABASE=location; UID=swaraj; PWD=Password@123;')
 
mysql = MySQL(app)

geolocator = Nominatim(user_agent="geoapiExercises")

@app.route('/')
def home():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM vehicle_details")
    # data = cur.fetchall()
    # cur.close()

    """"
    cursor = conn.cursor()	
    cursor.execute("SELECT latitude,longitude FROM roadconditiondb") 
    all = cursor.fetchall()
    length = len(all)


    cursor.execute("SELECT TOP 1* FROM roadconditiondb ORDER BY id DESC;")
    row = cursor.fetchall()
    lati = row[0][1]
    long = row[0][2]
 
    location = geolocator.reverse(str(lati)+","+str(long))
    return render_template("index.html",lati = lati, long = long, location = location, all = all, length = length)
"""
    return render_template("index.html")


@app.route('/main')
def maps():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM vehicle_details")
    # data = cur.fetchall()
    # cur.close()

    

    cursor = conn.cursor()	
    cursor.execute("SELECT latitude,longitude FROM roadconditiondb") 
    all = cursor.fetchall()
    length = len(all)


    cursor.execute("SELECT TOP 1* FROM roadconditiondb ORDER BY id DESC;")
    row = cursor.fetchall()
    lati = row[0][1]
    long = row[0][2]
 
    location = geolocator.reverse(str(lati)+","+str(long))

    return render_template("maps.html",lati = lati, long = long, location = location, all = all, length = length)


   



@app.route('/streetView')
def street():
    cursor = conn.cursor()	
    # cursor.execute("SELECT * FROM roadconditiondb") 
    cursor.execute("SELECT TOP 1* FROM roadconditiondb ORDER BY id DESC;")
    row = cursor.fetchall()
    lati = row[0][1]
    long = row[0][2]
    return render_template("street/street.html", lati = lati, long = long)


if __name__ == "__main__":
    app.run(debug = True)

 
