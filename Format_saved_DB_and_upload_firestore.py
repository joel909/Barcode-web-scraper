import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
cred = credentials.Certificate('C:/Users/joelj/Downloads/test/firestore-cred.json')
import json

firebase_admin.initialize_app(cred)
db = firestore.client()

def formatData(data):
    data =open(data,'r')
    for line in data:
        data = line
    frmd = json.loads(data)
    for i in range(0,len(frmd)):
        frmd[i] =str(frmd[i]).replace("'",'"')
    return frmd

data = "C:/Users/joelj/Downloads/Sample_Barcode_0.txt"
formatteddata = formatData(data)

docs = db.collection("merchants").document("352482").collection("barcodes").document("Barcodes")

docs.update({"barcodes":formatteddata})