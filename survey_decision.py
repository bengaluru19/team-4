from flask import Flask,request, abort
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)


@app.route('/submit_survey', methods=['POST'])
def hello_world():
	if not request.json:
		abort(400)
	r=request.get_json()
	customer_snake = request.json['user']['result_templates']
	customer_email = request.json['user']['email']
	print(r)
	print(customer_snake)
	#print(customer_snake[3:len(customer_snake-2)])
	customer_email=list(customer_email)
	customer_email.pop(0)
	customer_email.pop(0)
	customer_email.pop(-1)
	customer_email.pop(-1)
	customer_email="".join(str(e) for e in customer_email)
	customer_snake=list(customer_snake)
	customer_snake.pop(0)
	customer_snake.pop(0)
	customer_snake.pop(-1)
	customer_snake.pop(-1)
	customer_snake="".join(str(e) for e in customer_snake)
	print(customer_email,customer_snake)
	sender_email = "raghukapur9@gmail.com"
	receiver_email = customer_email[0]
	password = 'P@ssword0987'
	msg = MIMEMultipart()
	msg['From'] = sender_email
	msg['To'] = customer_email
	msg['Subject'] = "Project Design"
	body = "Thank you for taking out your time to complete our site survey! \n We hope you like the various playscape designs that we have specially curated for you based on your responses.Don’t hesitate to contact us if you have any queries.\nWe shall discuss further details with you over call shortly.\nWe are eager to work with you!"
	message = MIMEMultipart("alternative")
	msg.attach(MIMEText(body, 'plain'))
	filename = "{}".format(customer_snake)
	attachment = open("C:/xampp/htdocs/cfg/d1.jpg", 'rb')
	p = MIMEBase('application', 'octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(p)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(sender_email, "P@ssword0987")
	text = msg.as_string()
	s.sendmail(sender_email, "raghu.kapur2016@vitstudent.ac.in", text)
	s.quit()

	return (r)

"""
    sender_email = "raghukapur9@gmail.com"
    receiver_email = customer_email  
    password = 'P@ssword0987'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Welcome To Anthill Creations"
    message["From"] = sender_email
    message["To"] = receiver_email
    image_cid = make_msgid()

    html = """ \
"""    <html>
      <body>
        <p>Hello ,<br>
        Thank you for taking out your time to complete our site survey!<br>
We hope you like the various playscape designs that we have specially curated for you based on your responses. Don’t hesitate to contact us if you have any queries.<br>
We shall discuss further details with you over call shortly. We are eager to work with you!<br>
           <img src="cid:{image_cid}"><br>
           Sincerely,<br>
           Anthill Creations<br>
            NSRCEL, IIM Bangalore<br> 
            Bengaluru, Karnataka 560076<br> 
            India<br>
            +91.990.040.9202
        </p>
      </body>
    </html>
    .format(image_cid=image_cid[1:-1]), subtype='html')
"""
"""    with open('path/to/image.jpg', 'rb') as img:

        # know the Content-Type of the image
        maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

        # attach it
        msg.get_payload()[1].add_related(img.read(), 
                                             maintype=maintype, 
                                             subtype=subtype, 
                                             cid=image_cid)
"""
"""    # Turn these into plain/html MIMEText objects

    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

        server.sendmail(fromaddr, toaddrs, msg)  
        server.quit()

"""

if __name__ == '__main__':
	app.run(host='localhost', port='3001',debug = True)
