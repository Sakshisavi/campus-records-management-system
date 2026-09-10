from flask import Flask,render_template,request,redirect,url_for,flash,session,current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
from flask import Blueprint
from MySQLdb import IntegrityError


auth_bp = Blueprint("auth", __name__)



#config


@auth_bp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        dept = request.form['dept']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cur = current_app.extensions['mysql'].connection.cursor()
        try:
            cur.execute("INSERT INTO admins_record(Name,Department,Email,Password) VALUES(%s,%s,%s,%s)",
                    (name,dept,email,password)

            )
            current_app.extensions['mysql'].connection.commit()
            admin_id = cur.lastrowid   # <-- this gives you the new Admin_id
            flash(f"signup successful! Please login, Your Admin_id is {admin_id}")
            return redirect(url_for("auth.login"))
        except IntegrityError:
            flash("This email is already registered. Please use a different email.")
            return redirect(url_for("auth.signup"))
        finally:
            cur.close()

        
        
    return render_template('signup.html')

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        admin_id= request.form['admin_id']
        password = request.form['password']
        # Get MySQL connection from Flask app extensions
        cur = current_app.extensions['mysql'].connection.cursor()
        # Query the admins_record table
        cur.execute("SELECT Admin_id, Name, Password FROM admins_record WHERE Admin_id = %s", (admin_id,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[2], password):  
            # user[2] is the Password column
            session['user'] = user[1]   # store Name in session
            #flash("Login successful!")
            return redirect(url_for('index'))  # redirect to index.html route
        else:
            flash("Invalid Admin_id or password")

    return render_template('login.html')


      
          

@auth_bp.route('/profile')
def profile():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    cur = current_app.extensions["mysql"].connection.cursor()
    # Fetch all columns except password
    cur.execute("SELECT Admin_id, Name, Department, Email FROM admins_record WHERE Name = %s", (session["user"],))
    admin = cur.fetchone()
    cur.close()

    return render_template("profile.html", admin=admin)

@auth_bp.route('/logout')
def logout():
    session.pop("user", None)
    flash("You have been logged out.")
    return redirect(url_for("auth.login"))