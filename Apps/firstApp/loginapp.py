from flask import *

app = Flask(__name__)


@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        uname=request.form['uname']  
        passwrd=request.form['pass']  
        if uname=="adarsh71" and passwrd=="rawat123":  
            # return "Welcome %s" %uname  
            return render_template('welcome.html')
        else:
            return "<h1>Invalid Credentials</h1>"
        

# Same Approch Using Get Metho
# @app.route('/login',methods = ['GET'])  
# def login():  
#       uname=request.args.get('uname')  
#       passwrd=request.args.get('pass')  
#       if uname=="ayush" and passwrd=="google":  
#           return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  
if __name__ == '__main__':
    app.run(debug=True)
        