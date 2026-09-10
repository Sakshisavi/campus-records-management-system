from flask import Flask,render_template,request,redirect,url_for,session
from config import Config
from flask_mysqldb import MySQL
from auth import auth_bp
app = Flask(__name__)
#config
app.config.from_object(Config)

# Add a secret key (must be unique and secret)
app.secret_key = "your_super_secret_key_here"

mysql = MySQL(app)
app.extensions['mysql'] = mysql

app.register_blueprint(auth_bp)

@app.before_request
def clear_session_on_start():
    if request.endpoint == 'auth.login' and request.method == 'GET':
        session.pop("user", None)


@app.route("/")
def home():
    return redirect(url_for("auth.login"))

#read
@app.route('/index')
def index():
     # Protect index with a session check
    if "user" not in session:
        return redirect(url_for("auth.login"))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.close()
    return render_template('index.html', students=students)
#add
@app.route('/add', methods=['GET','POST'])
def add_student():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO students(name,email,course) VALUES(%s,%s,%s)",
            (name,email,course)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

                             
    return render_template('add.html')
#edit
@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit_student(id):
    cur = mysql.connection.cursor()

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        cur.execute(
            """ UPDATE students 
                SET name=%s, email=%s, course=%s
                WHERE id=%s
            """,(name,email,course,id)
        )
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))
    else:#For get request
        cur.execute("SELECT * FROM students where id =%s",(id,))
        student = cur.fetchone()
        cur.close
    return render_template('edit.html',student=student)
#delete
@app.route('/delete/<int:id>')
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s",(id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))
def Search():#Future feature that i will add Later
    pass
if __name__ == "__main__":
    app.run(debug=True)