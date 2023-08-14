from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit,QComboBox
from bs4 import BeautifulSoup
import requests

def get_current(in_currency,out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content,"html.parser")
    rate = soup.find("span",class_="ccOutputRslt").get_text()[:-4]
    return float(rate[:-4])

def show_currency():
    input_text = float(text.text())
    in_cur = in_combo.currentText()
    target_cur = target_combo.currentText()
    rate = get_current(in_cur,target_cur)
    output = round(input_text * rate,2)
    message = f"{input_text} {in_cur} is {output} {target_cur}"
    output_label.setText(str(message))


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency converter")

layout = QVBoxLayout()

in_combo = QComboBox()
currencies = ['USD','EUR','INR']
in_combo.addItems(currencies)
layout.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout.addWidget(target_combo)

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Convert")
layout.addWidget(btn)

btn.clicked.connect(show_currency)

output_label = QLabel("")
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()