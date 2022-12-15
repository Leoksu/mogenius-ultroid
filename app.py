import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'


# ex https://Leoksu:ghp_147bkkabcdefgh@github.com/Leoksu/Ultroid
# if u clone and rename the repo, then change 'Ultroid' to ur repo name

os.system("git clone https://username:token@github.com/username/Ultroid && cd Ultroid && pip3 install -r requirements.txt && pip3 install -r -U re*/st*/op* && python3 -m pyUltroid &")
