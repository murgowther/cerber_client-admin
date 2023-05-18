from flask import Flask, render_template, url_for, request, flash, session, redirect, g, abort
from config import host, port, database, user, password
from DataBase import DataBase
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = "2738a590569501f38f14871dbb6f9129a323deac4bc501f2cd"

def connect_db():
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password)
    conn.autocommit = True
    return conn


def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None


@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    datab = get_db()
    dbase = DataBase(datab)


@app.teardown_appcontext
def close_db(eror):
    '''Закрываем соединение с БД, когда происходит уничтожение контекста приложения,
    т.е. в момент завершения обработки запроса (если оно было установлено)'''
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.route('/index.html', methods=['POST', 'GET'])
def index():
    return render_template("index.html", title='Личный кабинет') 

@app.route('/zayavka.html', methods=['POST', 'GET'])
def zayavka():
    zayakvi = dbase.get_Zayavki()
    return render_template("zayavka.html", title='Заявки', zayakvi=zayakvi) 

@app.route('/error.html', methods=['POST', 'GET'])
def error():
    activ = dbase.get_all_activ()
    return render_template("error.html", title='Инциденты', a=activ) 

@app.route('/human.html', methods=['POST', 'GET'])
def human():
    pc = dbase.get_Zayavki()
    if request.method == "POST": 
        for f in request.form:
            activ = dbase.get_activ(f)
            secret_files = dbase.get_secretfiles(f)
            printers = dbase.get_printers(f)
            usb = dbase.get_usb(f)
            return render_template("human.html", title='Активность', pc=pc,activ=activ,sf=secret_files,p=printers,usb=usb) 
    return render_template("human.html", title='Активность', pc=pc) 

if __name__ == "__main__":
    app.run(debug=True)