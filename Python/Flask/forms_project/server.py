"""
This is about 1 , ,223,23,35454,54,
module wea re defining routes in Flask for class DEMO

"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)   

@app.route('/')                           
def registration():
    return render_template("index.html") 


@app.route('/users', methods=['POST'])                           
def create_user():
    print(request.form)
    f_name = request.form['first_name']
    l_name = request.form['last_name']
    return redirect('/on_success', first_name=f_name, last_name = l_name)


@app.route('/on_success')                           
def welcome_user():
    print(request.form)

    return render_template("success.html") 


if __name__=="__main__":
    app.run(debug=True) 