from flask import *

app = Flask(__name__)

@app.route('/error')
def error():
    return "<h1>User Does not Exist or Password is Invalid</h1>"


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "adarsh" and password == "pass123":
            response = make_response(render_template('success.html'))
            response.set_cookie('username', username)
            return response
        else:
            return redirect(url_for('error'))

@app.route("/viewprofile")
def viewprofile():
    username = request.cookies.get('username')
    response = make_response(render_template('viewprofile.html',username=username))
    return response 


if __name__ == "__main__":
    app.run(debug=True)
