from flask import *

app = Flask(__name__) # creating first instance of flask

@app.route('/') # decorator
def home():
    return "</h1>Hello World! This is my first flask app</h1>"

@app.route('/home/<name>') # decorator
def home2(name):
    return "<h1>Hello World! This is my first flask app, {}</h1>".format(name)


def about():
    return "<h1>THis is the about page</h1>"


app.add_url_rule("/about","about",about)

#########################URL BUILDING###########################################


@app.route('/admin')  
def admin():  
    return "<h1>I am admin</h1>"
  
@app.route('/librarion')  
def librarion():  
    return "<h1>I am librarian</h1>"
  
@app.route('/student')  
def student():  
    return "<h1>I am a student</h1>"  



@app.route('/user/<name>') # decorator
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))

    elif name == "librarian":
        return redirect(url_for('librarion'))

    elif name == "student":
        return redirect(url_for('student'))

    else :
        return "<h1>I am guest </h1>"

if __name__ == '__main__':
    app.run(debug=True) # run the app in debug mode
    


