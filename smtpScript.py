import smtplib
import datetime
import imaplib
import email

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "fromemail" + ORG_EMAIL
FROM_PWD    = "azertyuiop123456789"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

print "[+] Credentials added"
def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        print "[+] Success!, Connected."
        toaddrs = "towardsemail@gmail.com"
        msg = "email"
        try:
            SMTP_SERVER.set_debuglevel(1)
            SMTP_SERVER.sendmail(FROM_EMAIL, toaddrs, msg)
            SMTP_SERVER.quit()
        except Exception, h:
            print h
    except Exception, e:
        print str(e)

def main():
    read_email_from_gmail()

main()
