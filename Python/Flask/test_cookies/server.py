from flask import *  

app = Flask(__name__)  

@app.route('/cookie')  
def saad():  
  res = make_response("<h1>cookie is set in codeunderscored</h1>")  
  res.set_cookie('code','underscored', max_age=30)  
  res.set_cookie('interest','sport',max_age=10)  
  res.set_cookie('lang','en', max_age=10)  
  return res  

if __name__ == '__main__':  
  app.run(debug = True)  