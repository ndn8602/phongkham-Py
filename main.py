from flask import Flask, render_template, request, jsonify, redirect, url_for
from chat import get_response
import DAO

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('user/index.html')


@app.route('/admin', methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'GET':
        return render_template('admin/login.html', title='Admin Login')

    email = request.form['exampleInputEmail']
    password = request.form['exampleInputPassword']

    if DAO.loginAdmin(email, password) == False:
        return render_template('/admin/login.html', title='Admin Login', error='true')
    return redirect("/admin/home")


@app.route('/admin/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('admin/register.html', title='Admin Register')

    name = request.form['exampleFullName']
    email = request.form['exampleInputEmail']
    password = request.form['exampleInputPassword']

    if DAO.addAdmin(name, email, password) == False:
        return render_template('admin/register.html', title='Admin Register', error='true')
    return redirect("/admin")


@app.route('/admin/doctor', methods=['GET'])
def adminDoctor():
    doctors = DAO.getDoctors()
    return render_template('admin/admin_doctor.html', title='Admin Doctor', doctors=doctors)


@app.route('/admin/doctor/submit', methods=['POST'])
def doctorSubmitForm():
    # print(request.form)
    if request.method == 'POST':
        if 'add' in request.form:
            name = request.form['name']
            old = request.form['old']
            gender = request.form['gender']
            room = request.form['room']
            phone = request.form['phone']
            email = request.form['email']
            degree = request.form['degree']

            DAO.createDoctor(name, old, gender, room, phone, email, degree)

        if 'update' in request.form:
            doctor_id = request.form['id']
            name = request.form['name']
            old = request.form['old']
            gender = request.form['gender']
            room = request.form['room']
            phone = request.form['phone']
            email = request.form['email']
            degree = request.form['degree']

            DAO.updateDoctor(doctor_id, name, old, gender, room, phone, email, degree)
            # print(name,old,doctor_id,gender,room,phone,email,degree)
        elif 'remove' in request.form:
            doctor_id = request.form['id']

            # print(doctor_id)
            DAO.deleteDoctor(doctor_id)
        return redirect("/admin/doctor")


# @app.route('/admin/doctor/update', methods = ['POST'])
# def adminUpdateDoctor():
#     doctor_id = request.form['id']
#     name = request.form['name']
#     old = request.form['old']
#     gender = request.form['gender']
#     room = request.form['room']
#     phone = request.form['phone']
#     email = request.form['email']
#     degree = request.form['degree']

#     DAO.updateDoctor(doctor_id,name,old,gender,room,phone,email,degree) 

#     return redirect("/admin/doctor")
# doctor={
#     "id":request.form['id'],
#     "name":request.form['name'],
#     "old":request.form['old'],
#     "gender":request.form['gender'],
#     "room":request.form['room'],
#     "phone":request.form['phone'],
#     "email":request.form['email'],
#     "degree":request.form['degree'],
# }

# DAO.updateDoctor(doctor_id,name,old,gender,room,phone,email,degree)
# print(name,old,doctor_id,gender,room,phone,email,degree)

# doctors = DAO.getDoctors()
# return redirect("/admin/doctor")


@app.route('/admin/home')
def adminHome():
    return render_template('admin/index.html', title='Admin Home')


@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run()
