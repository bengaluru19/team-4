from flask import Flask, request, abort
import  smtplib
app = Flask(__name__)
@app.route('/test',methods=['POST'])
def hello_world():
    print(request.get_json())

    customer_name = request.json['user']['name ']
    customer_email = request.json['user']['email']
    customer_budget = request.json['user']['budget']
    fromaddr = 'raghukapur9@gmail.com'
    toaddrs = customer_email
    username = 'raghukapur9@gmail.com'
    password = 'P@ssword0987'
    server = smtplib.SMTP('smtp.googlemail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    customer_budget=list(customer_budget.split(" "))
    if (int(customer_budget[2]) < 50000):
        msg = 'Spam email Test'
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
    else:
        msg = 'Spam email Test'
        html = """\
        <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.realpython.com">Real Python</a> 
           has many great tutorials.
        </p>
      </body>
    </html>
    """
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

    return (request.get_json())

if __name__== '__main__':
   app.run(host='localhost',port='3000',debug=True)
