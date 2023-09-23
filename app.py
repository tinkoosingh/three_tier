from bs4 import BeautifulSoup
import requests
import mysql.connector
from flask import Flask, request, render_template, jsonify
from peewee import MySQLDatabase, IntegerField
import os 

MYSQL_ROOT_USER = os.getenv('MYSQL_ROOT_USER', 'root')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', 'test1234')
MYSQL_ROOT_HOST = os.getenv('MYSQL_ROOT_HOST', 'localhost')
MYSQL_ROOT_PORT = os.getenv('MYSQL_ROOT_PORT', '3306')
MYSQL_ROOT_DB = os.getenv('MYSQL_ROOT_DB', 'mydb')


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('front.html');

@app.route('/productData',methods=['POST'])
def productData():
    #args = request.args
    #rint(args)
    print("Stage 1 *****************************************")
    if request.method == "POST":
        product_name = request.form.get("name")
        num_of_pages = request.form.get("number")
        flipkart_url = "https://www.flipkart.com/search?q="+product_name+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+num_of_pages
        response = requests.get(flipkart_url)
        soup = BeautifulSoup(response.content,'html.parser')
        data = soup.find_all('div',{"class":"_1xHGtK _373qXS"})
        data_df = []
        conn = MySQLDatabase(database=MYSQL_ROOT_DB,user=MYSQL_ROOT_USER, password=MYSQL_ROOT_PASSWORD,
                    host=MYSQL_ROOT_HOST, port=int(MYSQL_ROOT_PORT))
        mycursor = conn.cursor()
        mycursor.execute("create database practice")
        mycursor.execute("create table flipkart(Product varchar(30), Details(200));")
        conn.commit()
        conn.close()
        print("stage 2 ***********************************************************************************")
        for text_data in data:
            conn = MySQLDatabase(database=MYSQL_ROOT_DB, user=MYSQL_ROOT_USER, password=MYSQL_ROOT_PASSWORD,
                    host=MYSQL_ROOT_HOST, port=int(MYSQL_ROOT_PORT))
            #mysql.connector.connect(user='root',host='mysql:3306', database='practice',password='test1234')
            mycursor = conn.cursor()
            sql = "INSERT INTO flipkart (Product, Details) VALUES (%s, %s)"
            fetched_data = text_data.get_text()
            data_df.append(fetched_data)
            val = (product_name, fetched_data)
            mycursor.execute(sql, val)
            conn.commit()
            conn.close()
  
    return jsonify(data_df)
        



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')





