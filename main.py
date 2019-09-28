from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def user_signup():
    return render_template('signup.html')



@app.route("/", methods=['POST'])
def user_response():

    # THIS CREATES VARIABLES FROM THE FORM INPUTS

    username = request.form['username']
    #password = request.form['password']
    #password_validate = request.form['password_validate']
    #email = request.form['email']
    username = username
    return redirect('/welcome?username={0}'.format(username))

@app.route("/welcome")
def signup_complete():
        username = request.args.get('username')
        return render_template('confirmation.html',username=username)
app.run()
