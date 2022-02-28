from flask import *


app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return render_template("home.html")

@app.route('/success',methods=['POST'])
def success():
    data = request.form
    return render_template("user_info.html",data=data)
    
if __name__ == '__main__':
    app.run(debug=True)