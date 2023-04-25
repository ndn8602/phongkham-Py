import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["phongkham"]
dbPatient = mydb["patient"]
dbDoctor = mydb["doctor"]
dbAdmin = mydb["admin"]

#create Chema


#patient={id:mongodb supported,name:string,old:number,gender:string,room:nameroom,phone:string,date:string} : All require
#doctor={id:mongodb supported,name:string,old:number,gender:string,room:nameroom,phone:string,degree:string,email:string {require:@},password:string} : All require
#room={id:mongodb supported, nameroom:string} : All require



#example
patient={
    'name':'ABCD',
    'old':12,
    'gender':'male',
    'room':'Heart',
    'phone':'012343645654' #length:10
}
doctor={
    'name':'ABCD',
    'old':12,
    'gender':'male',
    'room':'Heart',
    'phone':'012343645654', #length:10
    'email':'example@gmail.com',
    'degree':'ABCDS University'
}

# admin={
#     'name':'root',
#     'email': 'nomail@no',
#     'password': 'root', # can use bcrypto to hash password
# }

#handle here
def addNewDoctor():
    dbDoctor.insert_one(doctor)

def getDoctor():
    pass

def deleteDoctor():
    pass

def addPatient(patient):
    dbPatient.insert_one(patient)
def getPatients():
    pass
def addAdmin(name, email, password):
    admin={
        'name': name,
        'email': email,
        'password': password, # can use bcrypto to hash password
    }
    if dbAdmin.count_documents({'email': email}) != 0:
        return False
    dbAdmin.insert_one(admin)
    return True

def loginAdmin(email, password):
    if dbAdmin.count_documents({'email': email, 'password': password}) == 0:
        return False
    return True
# --- [DOCTOR] ----
def getDoctors():
    doctors = dbDoctor.find()
    return doctors
 
def updateDoctor(doctor_id,name,old,gender,room,phone,email,degree):
    print(name,old,doctor_id,gender,room,phone,email,degree)
    doctor_id = ObjectId(doctor_id)
    filter = {"_id": doctor_id}    
    update = {"$set": {
        "name": name,
        'old': old, 
        'gender': gender, 
        'room': room, 
        'phone': phone, 
        'email': email, 
        'degree': degree, 
    }}
    result = dbDoctor.update_one(filter, update)
    
 

def deleteDoctor(doctor_id):
    doctor_id = ObjectId(doctor_id)
    result = dbDoctor.delete_one({'_id': doctor_id})

def createDoctor(name,old,gender,room,phone,email,degree):
    doctor={
        'name': name,
        'old': old,
        'gender': gender,
        'room': room,
        'phone': phone,
        'email': email,
        'degree': degree,
    }
    dbDoctor.insert_one(doctor)

# --- [PATIENT] ----

def getPatients():
    petient = dbPatient.find()
    return petient


def createPateint(pateint):
    dbPatient.insert_one(pateint)

 
def updatePatient(patient_id,patient):
    print("dao.update")
    print(patient_id,patient)
    patient_id = ObjectId(patient_id)
    filter = {"_id": patient_id}    
    update = {"$set": {
        "name":patient['name'],
        "gender": patient['gender'],
        "room": patient['room'],
        "phone": patient['phone'],
        "email":patient['email'],
        "address":patient['address'],
        "date":patient['date'],
    }}
    print(update)
    result=dbPatient.update_one(filter, update)
    print(result.modified_count)
    
 


def deletePatiet(pateint_id):
    print("dao.delete")
    pateint_id = ObjectId(pateint_id)
    dbPatient.delete_one({'_id': pateint_id})
