# Text Extractor
*A django application to extract text from single page pdf and images.*

## How it works
![diagram](/screenshot/working.png)

## Feature and Limitations
- Works also with scanned pdf
- Works with only single page pdf

## Prerequisite and Installation guide
- imageMagick (should be installed in your system)
- Ghostscript (need to be installed in your system)
- Tesseract-OCR (need to be installed in your system)
- __make sure environment variable of all the above is set correctly.__

### Steps
- Create a virtual environment
- install the requirements from the requirements.txt file
- setup postgres db or comment the postgres db setting and uncomment the sqlite db settings in settings.py file
- run the server

## Screenshots
### Home Page
![](/screenshot/127.0.0.1_8000_.png)
### Details Page
![](/screenshot/127.0.0.1_8000_1_.png)
### SignIn Page
![](/screenshot/127.0.0.1_8000_accounts_login_.png)

[Demo Video](https://youtu.be/oblnol8GkoQ)
