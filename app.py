import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'


#ex https://Leoksu:ghp_147bkkabcdefgh@github.com/Leoksu/Ultroid
#note : change reponame with your Ultroid fork repo and don't forget to create .env file with all filled vars 

os.system("git clone https://username:token@github.com/username/reponame && cd Ultroid && pip install -r requirements.txt && pip install -r resour*/start*/optiona*.txt && python3 -m pyUltroid &")
