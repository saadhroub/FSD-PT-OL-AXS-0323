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
    if request.form['which_form'] == 'register':
        print(request.form)
        session['f_name'] = request.form['first_name']
        session['l_name'] = request.form['last_name']
        session['user_email'] = request.form['email']
        session['dob'] = request.form['birthdate']
        session['user_password'] = request.form['password']
        session['c_password'] = request.form['confirm_password']
        session['gender'] = request.form['gender']
        return redirect("/success_reg")
    
    elif request.form['which_form'] == 'login':
        session['email'] = request.form['email']
        return redirect("/success_log")
 

@app.route('/success_reg')                           
def reg_result():
    first_name = session['f_name']
    print(request.form)
    return render_template("success_reg.html", first_name = first_name) 


@app.route('/success_log')                           
def log_result():
    first_name = session['f_name']
    print(request.form)
    return render_template("success_log.html", first_name = first_name) 


# How to clear session data ?
# session.clear()	
# session.pop('key_name')		


if __name__=="__main__":
    app.run(debug=True) 