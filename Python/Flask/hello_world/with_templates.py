from flask import Flask, render_template 
app = Flask(__name__)   

@app.route('/')                           
def first_template():
    return render_template('welcome.html') 

@app.route('/login')                           
def data_on_template():
    return render_template("user.html", my_ninja = "Kareem", my_age = 22, my_stack = "Python") 




@app.route('/academy/courses')
def show_courses():
    my_courses = ['Mathematics','Physics','Chemistry','Biology',
                'Computer Science','AI','Accounting','Arabic', 'English Levels 1- 4'
                 ]
    return render_template("courses.html", courses = my_courses )

if __name__=="__main__":
    app.run(debug=True)  
