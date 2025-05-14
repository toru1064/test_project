from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    books = [
        # {'title': 'はらぺこリン',
        # 'price': '1200',
        # 'arrival_day': '2020/7/9'},
        # {'title': 'ハリーポッター',
        # 'price': '2500',
        # 'arrival_day': '2020/12/12'}
    ]
    return render_template("index.html",books=books)

@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
