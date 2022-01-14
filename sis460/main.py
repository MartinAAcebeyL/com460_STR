import time

from flask import Flask, render_template
import threading
from funciones import *
import jyserver.Flask as js

app = Flask(__name__)

TEMPERATURA = 0
LISTA_I = [14, 15, 16]
RELOJ = 'reloj'

@js.use(app)
class App:
    @js.task
    def main_ajax(self):
        while True:
            #temperatura
            self.js.document.getElementById('t1').value = LISTA_I[0]
            self.js.document.getElementById('t1').style.backgroundColor = 'green' if LISTA_I[0]<38 else 'red'

            self.js.document.getElementById('t2').value = LISTA_I[1]
            self.js.document.getElementById('t2').style.backgroundColor = 'green' if LISTA_I[1] < 38 else 'red'

            self.js.document.getElementById('t3').value = LISTA_I[2]
            self.js.document.getElementById('t3').style.backgroundColor = 'green' if LISTA_I[2] < 38 else 'red'
            #reloj
            self.js.document.getElementById('reloj').innerHTML = RELOJ


def temperaturas_():
    global TEMPERATURA
    while True:
        TEMPERATURA = temperatura()
        LISTA_I.append(TEMPERATURA)
        LISTA_I.pop(0)
        time.sleep(1.5)

def reloj_():
    global RELOJ
    day = 0
    hour = 0
    min = 0
    sec = 0

    while True:
        time.sleep(1)
        if sec == 59:
            sec = -1
            min = min + 1
        sec = sec + 1
        if min == 60:
            min = 0
            hour = hour + 1
        if hour == 24:
            hour = 0
            day = day + 1
        RELOJ = f'{day}:{hour}:{min}:{sec}'

@app.route("/")
def index():
    return App.render(render_template('index.html'))


if __name__ == '__main__':
    thread_temperatura = threading.Thread(target=temperaturas_, daemon=True)
    thread_temperatura.start()
    thread_tiempo = threading.Thread(target=reloj_, daemon=True)
    thread_tiempo.start()

    App.main_ajax()
    app.run(debug=True)
