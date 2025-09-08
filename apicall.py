import requests
# print(requests)

apiUrl = "http://fakestoreapi.com/products"
data = requests.get(apiUrl)
print(data)

class fakeStoreApi:
    def __init__(self,t,p):
        # print(t,"is of price",p)
        pass
    def products(self,t,p):
        print(t,"is of price ",p)
    
if data.status_code == 200:
    mainData = data.json()
    # print(mainData)
    for i in mainData:
        title = i["title"]
        price = i["price"]
        
        details=fakeStoreApi(title,price)
        details.products(title,price)
    
    



