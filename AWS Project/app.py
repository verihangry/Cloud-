from flask import Flask, render_template, request, url_for, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'han123'  # Needed for session management

# Get connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Get user information
def get_user_info(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username = ?", (username,))
    data = cur.fetchall()
    return data

# Home page route
@app.route("/")
def home():
    return render_template("login.html")

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        pw = request.form["password"]

        user = get_user_info(us)
        for item in user:
            username = request.form['username']
            if username != item[0]:
                error = "username don't have account"
                return redirect('login', error = error)
            elif pw != item[1]:
                error = "invalid password"
            else:
                ms = "You are successfully logged in"
                session[username] = us
                return render_template('result.html', user = user, ms = ms)
            return render_template('login.html', error = error)

# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            conn = get_db_connection()
            username = request.form['username']
            password = request.form['password']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            cur = conn.cursor()
            cur.execute("INSERT INTO user (username, password, firstname, lastname, email) VALUES (?, ?, ?, ?, ?)", (username, password, firstname, lastname, email))
            con.commit()

            ms = "Logged in sucessfully"
        except:
            error = "You already have the account"
            return render_template('login.html', error = error)
        data = get_user_info(username)
        return render_template('result.html', data = data, ms=ms)
# Result page (after login)
@app.route("/result")
def result():
    if 'username' in session:
        return f"Welcome {session['username']}! <br><a href='/logout'>Logout</a>"
    return redirect(url_for("login.html"))

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.html'))

if __name__ == '__main__':
    app.run(debug=True)
