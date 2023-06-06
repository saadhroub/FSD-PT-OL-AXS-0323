"""
This is application for teaching sessions impact
"""

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'P@55w0rd' # set a secret key for security purposes



@app.route('/')                           
def registration():
    return render_template("index.html") 


'''Redirect functions explanation, this method redirects work to another route
the new route aims to avoid re-submission of the form, but no data there 
'''
@app.route('/users', methods=['POST'])                           
def create_user():
    print(request.form)
    session['f_name'] = request.form['first_name']
    session['l_name'] = request.form['last_name']
    session['dob'] = request.form['birthdate']
    session['gender'] = request.form['gender']
    return redirect("/on_success") 


''' This route triggers a method that welcomes the user but it shows 
    empty data because the HTTP request/response cycle is stateless, 
    each response has not idea about the other
'''
@app.route('/on_success')                           
def welcome_user():
    name = session['f_name'] + ' ' + session['f_name']
    if 'counter' in session:
        session["counter"] += 1
    else:
        session["counter"] = 0
    x = session["counter"]


    return render_template("success.html", full_name = name, counter=x) 



@app.route('/reset_visitors', methods =['POST'])                           
def reset():
    if 'counter' in session:
        session['counter'] = 0
    return redirect('/on_success') 


# How to clear session data ?
# session.clear()	
# session.pop('key_name')		


if __name__=="__main__":
    app.run(debug=True) 