from flask import Flask,render_template,request,jsonify,make_response
app = Flask(__name__)

@app.route('/')
def hello_two():
   a = {
   "name":"\\David", 
   "age":"12",
   "addre":"2332"
   }
   return a

if __name__ == '__main__':
   app.run(debug=True)