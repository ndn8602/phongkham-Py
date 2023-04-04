from flask import Flask,render_template,request,jsonify,redirect,url_for
from chat import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user/index.html')

@app.route('/admin/')
def adminLogin():
    return render_template('admin/login.html' ,title='Admin Login')

@app.post('/admin/register/createadmin')
def addAdmin():
    name = request.form['exampleFullName']
    
    if name == 'err':
        return render_template('admin/register.html' ,title='Admin Register',error='true')
    return redirect("/admin")

@app.route('/admin/register/')
def register():
    return render_template('admin/register.html' ,title='Admin Register')

@app.route('/admin/home')
def adminHome():
    return render_template('admin/index.html',title='Admin Home')

@app.post('/predict')
def predict():
    text=request.get_json().get('message')
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

if __name__ == "__main__":
    app.run()
