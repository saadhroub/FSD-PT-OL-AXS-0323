from flask import Flask, render_template
app = Flask(__name__)   


@app.route('/')          
def hello_world():
    return "Welcome to AXSOS Academy"

@app.route('/stacks')
def list_stacks():
    return '''
            <h1>I am studying the following stacks:</h1>
            <ol>
                <li>WEb Fundamentals</li>
                <li>Python</li>
                <li>Java</li>
            </ol>'''


@app.route('/careers/<job>/<salary>') 
def show_career_salary(job, salary):
    return "<h3>My CAreer: " + job + "</h3> <h4> My salary: " + salary + " USD/Month </h4>"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

