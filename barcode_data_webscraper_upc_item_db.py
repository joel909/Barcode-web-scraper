import requests
from bs4 import BeautifulSoup 
import html5lib
import json

name = ["tea","coffee","milk","bar","chips","juice","biscuit","cake","rice","pasta","bread"]
l1 = []

def getbarcode(soup):
    all_barcodes = []
    barcodes = soup.find_all("a",attrs={"class":"img"})
    for barcode in barcodes:
        all_barcodes.append(barcode["href"].split("c/")[1])
    return all_barcodes

def getproductnames(soup):
    product_names=[]
    product_nameshtml =soup.find_all("p")
    del product_nameshtml[0]
    print(product_nameshtml)
    for product_name in product_nameshtml:
        product_names.append(product_name.text)
    return product_names

data = []

for i in name:
    response = requests.get(f"https://www.upcitemdb.com/info-{i}")
    soup = BeautifulSoup(response.content)
    Barcodes = getbarcode(soup)
    prod_name = getproductnames(soup)
    for i in range (0,len(prod_name)-1):
        #print(i)
        data.append({"id":str(Barcodes[i]),"name":(prod_name[i].replace("'",'')),"price":str(i),"HSN":"1525343423222","category":"Chips"})

print(f"GOT {len(data)} BARCODE ITEMS")

# Write the JSON list to a file
filename = "Sample_Barcode_0.txt"
with open(filename, "w") as file:
    json.dump(data, file)

