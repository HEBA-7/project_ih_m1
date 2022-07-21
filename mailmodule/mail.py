import smtplib
import imghdr
from email.message import EmailMessage
def mailing():

    Sender_Email = "halima.elbadoui@gmail.com"
    Reciever_Email = "halima.elbadoui@gmail.com"
    Password = 'rwyimdcgusfiuxft'
    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Check out the distance of school" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Hey, here you have the distance from your school to the closet Bicimad tation!') 
    files = ['bicimad_coles_escuelas.csv']


    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = file
        newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)