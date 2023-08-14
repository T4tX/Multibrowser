from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/search', methods=['POST'])
def search():
    search = request.form.get('search')
    if search != '':
        print(search)
    else:
        print('dsfsdf',search)
    return render_template("search.html", text_for_search=search)


if __name__ == '__main__':
    app.run(debug=True)
