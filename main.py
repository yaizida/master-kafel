import requests
import telegram
from flask import Flask, request
from flask import render_template


TELEGRAM_TOKEN = '6418803145:AAHnNKWgvsQR130qxTQUSt09ZOAoRe6v2zM'
CHAT_ID = '853168658'

bot = telegram.Bot(token=TELEGRAM_TOKEN)

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def hello():
    if request.method == 'POST':
        phonenumber = request.form.get('phone_number')
        print('получен номер', phonenumber)
        name = request.form.get('name')
        print('получено имя', name)
        text = f'!!! ПОСТУПИЛА ЗАЯВКА !!!\n{phonenumber}\n{name}'
        if name != '' and phonenumber != '':
            requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text} ')
    return render_template('index.html')


app.run()
