from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests

def get_current(in_currency,out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content,"html.parser")
    print(soup)
    currency = soup.find("span",class_="ccOutputRslt")
    print(currency)
    rate = soup.find("span",class_="ccOutputRslt").get_text()[:-4]
    return float(rate)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Currency Rate API</h1><p>Example URL: /api/v1/usd-eur</p>"

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_current(in_cur,out_cur)
    result_dictionary = {"input_currency":in_cur,"output_currency":out_cur,"rate":rate}
    return jsonify(result_dictionary)

app.run(host='0.0.0.0')