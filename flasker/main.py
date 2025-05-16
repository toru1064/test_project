from flask import Flask, render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()
    con.close()

    books = [
        {'title': 'はらぺこリン',
        'price': '1200',
        'arrival_day': '2020/7/9'},
        {'title': 'ハリーポッター',
        'price': '2500',
        'arrival_day': '2020/12/12'}
    ]

    for row in db_books:
        books.append({'title': row[0], 'price': row[1], "arrival_day": row[2]})

    return render_template("index.html",books=books)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/register",methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?, ?, ?)',
                [title, price, arrival_day])
    con.commit()
    con.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
