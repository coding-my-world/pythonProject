# 崔浩然
# 时间:2021/9/26 14:39
# 功能:Flask服务
from flask import Flask
import time
app=Flask(__name__)

@app.route('/python')
def index_bobo():
    time.sleep(2)
    return 'Hello Python'

@app.route('/Diga_Altman')
def index_Diga_Altman():
    time.sleep(2)
    return 'Bye Diga Altman'

@app.route('/guang')
def index_guang():
    time.sleep(2)
    return 'do you believe guang'

if __name__=='__main__':
    app.run(threaded=True)