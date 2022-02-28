from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save("profiles/"+f.filename)  
        image_file=url_for('static',filename='profiles/'+ f.filename)
    	return render_template('success', title='Account',image_file=image_file)

  
if __name__ == '__main__':  
    app.run(debug = True) 
