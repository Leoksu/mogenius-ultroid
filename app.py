import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://github.com/TeamUltroid/Ultroid && cd Ultroid && bash installer.sh && cp ../.env .env && bash startup &")

