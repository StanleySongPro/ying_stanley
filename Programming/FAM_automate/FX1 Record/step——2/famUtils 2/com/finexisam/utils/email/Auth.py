import imaplib

class MailAuth(object):

    def __init__(self, username,password,using_email=None,server=None,port=None):
        '''
        Constructor
        '''
        self.username = username
        self.password = password
        if (using_email):
            self.using_email = using_email
        if (server):
            self.smtp_server = server
        else:
            self.smtp_server = "smtp.office365.com"
        if (port):
            self.smtp_port = port
        else:
            self.smtp_port = 587
            
    def mail(self):
        if (self.mail):
            return self.mail
        self.mail = imaplib.IMAP4_SSL(self.smtp_server)
        self.login_user = self.username+"\\" + self.using_email
        self.mail.login(self.login_user,self.password)
        return self.mail
    
    def logout(self):
        self.mail.close()
        self.mail.logout()
        self.mail = None;
        
        
        