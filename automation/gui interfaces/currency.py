from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from bs4 import BeautifulSoup
import requests

def get_current(in_currency='USD',out_currency='EUR'):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content,"html.parser")
    rate = soup.find("span",class_="ccOutputRslt").get_text()[:-4]
    return float(rate[:-4])

def show_currency():
    input_text = float(text.text())
    rate = get_current()
    output = round(input_text * rate,2)
    output_label.setText(str(output))


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency converter")

layout = QVBoxLayout()

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