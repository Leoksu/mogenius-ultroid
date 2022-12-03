import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#get your github token in https://github.com/settings/tokens

#Ex https://Leoksu:ghp_147bkkabcdefgh@github.com/Leoksu/Ultroid
os.system("git clone https://username:token@github.com/username/reponame && cd Ultroid && pip install -r requirements.txt && pip install -r resour*/start*/optiona*.txt && python3 -m pyUltroid &")
