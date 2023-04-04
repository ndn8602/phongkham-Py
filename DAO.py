import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["phongkham"]
dbPatient = mydb["patient"]
dbDoctor = mydb["doctor"]
dbAdmin = mydb["admin"]

#create Chema


#patient={id:mongodb supported,name:string,old:number,gender:string,room:nameroom,phone:string} : All require
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

def addPatient():
    dbPatient.insert_one(patient)

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

#test

addNewDoctor()
addPatient()
# addAdmin()