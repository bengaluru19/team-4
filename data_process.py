import mysql.connector
from flask import Flask

#####Getting the data from survet page

app = Flask(__name__)
@app.route('/schedule_data',methods=['GET'])
def hello_world():
    ####Connecting to the database
    if not request.json:
        abort(400)
    print(request.get_json())
    snake = request.json['data']['duration']['start_time']
    area = request.json['data']['duration']['end_time']
    budget =request.json['data']['duration']['end_time']
    mydb = mysql.connector.connect(host="localhost",user="yourusername",passwd="yourpassword")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM customers WHERE snake='{}',area={},budget={}".format(snake,area,budget)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
   return("Completed")



if __name__ == '__main__':
   app.run()


