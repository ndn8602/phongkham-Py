import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["phongkham"]
dbPatient = mydb["patient"]
dbDoctor = mydb["doctor"]

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
    'password':'123admin', # can use bcrypto to hash password
    'degree':'ABCDS University'
}

#handle here

def addNewDoctor():
    dbDoctor.insert_one(doctor)

def getDoctor():
    pass

def deleteDoctor():
    pass

def addPatient():
    dbPatient.insert_one(patient)


#test

addNewDoctor()
addPatient()