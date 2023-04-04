from flask import Flask,render_template,request,jsonify,redirect,url_for
from chat import get_response
import DAO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user/index.html')

@app.route('/admin', methods = ['GET', 'POST'])
def adminLogin():
    if request.method == 'GET':
        return render_template('admin/login.html' ,title='Admin Login')

    email = request.form['exampleInputEmail']
    password = request.form['exampleInputPassword']
    
    if DAO.loginAdmin(email, password) == False:
        return render_template('/admin/login.html',title='Admin Login',error='true')
    return redirect("/admin/home")

@app.route('/admin/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('admin/register.html' ,title='Admin Register')
    
    name = request.form['exampleFullName']
    email = request.form['exampleInputEmail']
    password = request.form['exampleInputPassword']
    
    if DAO.addAdmin(name, email, password) == False:
        return render_template('admin/register.html' ,title='Admin Register',error='true')
    return redirect("/admin")

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
