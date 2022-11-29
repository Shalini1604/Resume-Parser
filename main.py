import dotenv
import os
import email_extraction
import pdfminer_multiple
import resume
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
print("**************Welcome to MATRIX Resume Scanner**********")
while True:
    os.environ["API_PATH_PDF"] = input("Enter the path where you want to save the resumes: ")

    dotenv.set_key(dotenv_file, "API_PATH_PDF", os.environ["API_PATH_PDF"])
    path=os.environ["API_PATH_PDF"]
    if not os.path.exists(path+'/'):
        val=input("This directory does not exist, Enter path again (yes or no) ")
        if val.lower()=="yes":
            continue
        elif val.lower()=="no":
            val1=input("Do you want to create  directory in this path (yes or no) ")
            if val1.lower()=="yes":
                os.mkdir(path+'/')
                email_extraction.attachment_download(path)
                break
            elif val1.lower()=="no":
                exit()
            else:
                print("Invalid input")
        else:
             print("Enter either yes or no only")

    elif os.path.exists(path+'/'):

        email_extraction.attachment_download(path)
        break
 

os.environ["API_PATH_TXT"] = input("Enter the path where you want to save converted text files:  ")

dotenv.set_key(dotenv_file, "API_PATH_TXT", os.environ["API_PATH_TXT"])
pdfDir = os.environ["API_PATH_PDF"] + '/'
txtDir = os.environ["API_PATH_TXT"] +'/'
pdfminer_multiple.convertMultiple(pdfDir, txtDir)

resume.scanner(os.environ["API_PATH_TXT"] +'/')


