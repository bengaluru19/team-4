from flask import Flask, request, abort
import  smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
@app.route('/test',methods=['POST'])
def hello_world():
    print(request.get_json())
    customer_email = request.json['user']['email']
    sender_email = "raghukapur9@gmail.com"
    receiver_email = customer_email
    password = 'P@ssword0987'
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = customer_email
    msg['Subject'] = "Project Design"
    body = "Thank you for contacting us at Anthill Creations.\n Sorry we don't take orders less than Rs.100000.\nPlease Contact AntHill Creations for Fundraises.\n https://www.google.com"
    message = MIMEMultipart("alternative")
    msg.attach(MIMEText(body, 'plain'))
    filename = "helpage-brochure.pdf"
    attachment = open("C:/Users/RAGHU/Downloads/helpage-brochure.pdf", 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, "P@ssword0987")
    text = msg.as_string()
    s.sendmail(sender_email, receiver_email, text)
    s.quit()
    return(customer_email)
"""
    customer_name = request.json['user']['name ']
    customer_email = request.json['user']['email']
    customer_budget = request.json['user']['budget']
    fromaddr = 'raghukapur9@gmail.com'
    toaddrs = customer_email
    print(customer_email)
    username = 'raghukapur9@gmail.com'
    password = 'P@ssword0987'
    server = smtplib.SMTP('smtp.googlemail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    if (customer_budget =="less than 100000"):
        msg = '''   Thank you for contacting us at Anthill Creations.
        Sorry we don't take orders less than Rs.100000.
        Please Contact AntHill Creations for Fundraises.
        https://www.google.com
        '''
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
    else:
        htt = 'Spam email Test working'
        msg = '''
            Thank you for registering with us at Anthill Creations.
        We are excited to have you support our endeavours of bringing back play for all age groups by constructing sustainable playscapes, using contextual designs and localized resources and encouraging community participation.
        To complete the on-boarding, please click on the below link to complete a 10 minute site survey.
        https://www.google.com
        We are looking forward to making our working relationship a success.
        Sincerely,
        Anthill Creations
        NSRCEL, IIM Bangalore
        Bengaluru, Karnataka 560076
        India
        '''
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
"""
    

if __name__== '__main__':
   app.run(host='localhost',port='3000',debug=True)
