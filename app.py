import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://github.com/TeamUltroid/Ultroid && cd Ultroid && pip3 install -r requirements.txt && pip3 install -r re*/st*/op* && cp ../.env .env && bash startup &")

