import smtplib

class EmailAuth:
    def __init__(self,my_email,password,destination_email,msg):
        print("Sending an email...")
        self.my_email = my_email
        self.password = password
        self.destination_email = destination_email
        self.msg = msg
    def __enter__(self):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.starttls()
            self.server.login(self.my_email,self.password)
        except:
            print("Email authorization failed")
    def __exit__(self, type, value, traceback):
        self.server.quit()
        print("Sending message succeeded")
    def send_email(self):
        self.server.sendmail(self.my_email, 
                        self.destination_email, 
                        self.msg)
        

