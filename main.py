from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('signup.html')

    return redirect('confirmation.html',user_name=request.get['user-name'])
app.run()
