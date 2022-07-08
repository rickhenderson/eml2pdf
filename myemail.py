# My Email Program
# Rick Henderson - July 7, 2022
# Import smtplib for the actual sending function
import smtplib
from email.message import EmailMessage
from email.parser import BytesParser, Parser
from email.policy import default

messageFile = "eml2.eml"

def walkMessage(aMsg):

    for part in aMsg.walk():
        print(part.get_content_type())

def getMessage(textFile):
    with open(textFile) as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())
    return msg

def basicSample():
    with open(messageFile) as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = f'The contents of {textfile}'
    msg['From'] = "rihenderson@blackberry.com"
    msg['To'] = "rihenderson@blackberry.com"

    # Send the message via our own SMTP server. Needs to be running. Write your own?
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

def basicSample2():
    # If the e-mail headers are in a file, uncomment these two lines:
    with open(messageFile, 'rb') as fp:
        headers = BytesParser(policy=default).parse(fp)

    #  Now the header items can be accessed as a dictionary:
    print('To: {}'.format(headers['to']))
    print('From: {}'.format(headers['from']))
    print('Subject: {}'.format(headers['subject']))

    # You can also access the parts of the addresses:
    print('Recipient username: {}'.format(headers['to'].addresses[0].username))
    print('Sender name: {}'.format(headers['from'].addresses[0].display_name))

def main():
    print("\n\n (( A Basic Email Program ))\n")
    basicSample2()


if __name__ == '__main__':
    main()
