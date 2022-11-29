import pdfminer_single
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import PyPDF2
import os
import sys, getopt

#requireent- all pdfs and texts in the pdf folder should be resumes... tghats why its better not to
#requirement-text folder should be empty
#converts pdf, returns its text content as a string
def convertMult(pdfDir, txtDir):
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
            fileExtension = pdf.split(".")[-1]
            if fileExtension == "pdf":
                pdfFilename = pdfDir + pdf
                text = pdfminer_single.convert(pdfFilename) #get string of text content of pdf
                textFilename = txtDir + pdf + ".txt"
                if os.path.exists(textFilename):
                    while True:
                        val=input("file " +textFilename +" File already exists ! Do you want to overwrite (yes/no)(no-quit)")#testing
                        if val.lower()=="yes":
                            textFile = open(textFilename, "w") #make text file
                            textFile.write(text) #write text to text file
                            break
                        elif val.lower()=="no":
                            exit()
                        else:
                            print(" Enter either yes or no only ")
                            continue
                else:
                    textFile = open(textFilename, "w") #make text file
                    textFile.write(text) #write text to text file        
        
                        
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    if os.path.exists(pdfDir) and os.path.exists(txtDir) :
        convertMult(pdfDir, txtDir)
                #textFile.close
    else:
        if not os.path.exists(txtDir):  #testing
            while True:
                val=input(" this directory does not exist do you want to create one (yes/no) (no-quit program)")   #testing
                if val.lower()=="yes":
                    os.mkdir(txtDir)
                    convertMult(pdfDir, txtDir)
                    break
                elif val.lower()=="no":
                    exit()
                else:
                    print(" Enter either yes or no only ")
                    continue
        else:
            print(" Given directory does not exist ")

