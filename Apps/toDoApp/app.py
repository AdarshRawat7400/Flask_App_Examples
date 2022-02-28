from flask import *
from decouple import config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  config('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config('TRACK_MODIFICATIONS')
db = SQLAlchemy(app)

class ToDo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    

@app.route('/')
def index():
    todo_list = ToDo.query.order_by(ToDo.id.desc()).paginate(per_page=4, error_out=True)
    # print(todo_list)
    return render_template('base.html',todo_list = todo_list)

@app.route('/pageno/<int:page_num>')
def pageno(page_num):
    todo_list = ToDo.query.order_by(ToDo.id.desc()).paginate(per_page=4,page=page_num, error_out=True)
    return render_template('base.html',todo_list = todo_list)

################ Add EndPoint ########################
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_todo = ToDo(title=title,complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

############### Update EndPoint ########################
@app.route('/update/<int:todo_id>',methods = ['GET'])
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))


##################### Delete EndPoint ########################
@app.route('/delete/<int:todo_id>',methods = ['GET'])
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    db.create_all()
    # todo_task = ToDo(title='Learn Flask', complete=False) # created a task manually
    # db.session.add(todo_task)
    # db.session.commit()
    app.run(debug=True)

