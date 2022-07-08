#!/usr/bin/python
import argparse
import email
from email.message import EmailMessage
from email.parser import BytesParser, Parser
from email.policy import default
import os
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict
import re
import time

messageFile = "eml1.eml"
message2 = "eml2.eml"
message3 = "Simple Email with Text Attachment.eml"
message4 = "Free Live Event Secure Systems Start with Foundational Hardware.eml"
message5 = "Simple Image Attached.eml"
outputFilename = "emaillist.csv"
dir_path = 'C:\\Users\\rihenderson\\Desktop\\eml2pdf'

# Borrowed from Didier Stevens' pdf-parser
CHAR_WHITESPACE = 1
CHAR_DELIMITER = 2
CHAR_REGULAR = 3

CONTEXT_NONE = 1
CONTEXT_OBJ = 2
CONTEXT_XREF = 3
CONTEXT_TRAILER = 4

PDF_ELEMENT_COMMENT = 1
PDF_ELEMENT_INDIRECT_OBJECT = 2
PDF_ELEMENT_XREF = 3
PDF_ELEMENT_TRAILER = 4
PDF_ELEMENT_STARTXREF = 5
PDF_ELEMENT_MALFORMED = 6

class cPDFfile:
    __name = ''
    __PDFHEADER = '%PDF1.7'

    def __init___(self,name):
        # Constructor is always called.
        # Self passes a reference of the actuall object currently calling the method
        self.__name = name
        pass
    
def Timestamp(epoch=None):
    if epoch == None:
        localTime = time.localtime()
    else:
        localTime = time.localtime(epoch)
    return '%04d%02d%02d-%02d%02d%02d' % localTime[0:6]

def printHeaders(headers):
    #  Now the header items can be accessed as a dictionary:
    print('To: {}'.format(headers['to']))
    print('From: {}'.format(headers['from']))
    print('Subject: {}'.format(headers['subject']))

    # You can also access the parts of the addresses:
    print('Recipient username: {}'.format(headers['to'].addresses[0].username))
    print('Sender name: {}'.format(headers['from'].addresses[0].display_name))

def printColumnHeadings():
    return "recipient,sender,message-id"

def formatHeaders(headers):
    messageRow = f"{headers['to']},{headers['from']},{headers['message-id']}"
    return messageRow

def outputToCSV(messageList):
    print("\n[+] Printing emaillist.csv")

    with open(os.path.join(dir_path, outputFilename), 'w') as fp:
        fp.write(printColumnHeadings())
        fp.write("\n")
        fp.write(messageList)

def main():
    messageList = ""
    numberOfEmailMessages = 0
    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    printColumnHeadings()
    for file in res:
        # Check if the file is an .eml file
        if file.endswith('.eml'):
            numberOfEmailMessages += 1
            with open(file, 'rb') as fp:
                headers = BytesParser(policy=default).parse(fp)
                # We can extract the richest alternative in order to display it:
                richest = headers.get_body()
                partfiles = {}
                if richest['content-type'].maintype == 'text':
                    #print("type=text")
                    pass
                    if richest['content-type'].subtype == 'plain':
                        #print("subtype=plain")
                        pass

                print(formatHeaders(headers))
                messageList += formatHeaders(headers)
                #printHeaders(headers)
    outputToCSV(messageList)
    print(f"[+] Processed {numberOfEmailMessages} .eml messages.")

# Execute the main program
if __name__ == '__main__':
    print('\n[+] Main will be executed...')
    main()
