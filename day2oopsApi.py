
import requests
# print(requests)
apiUrl = " https://jsonplaceholder.typicode.com/users"
response = requests.get(apiUrl)
# print(response)

class jsonPlaceholderApi:
    
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
        
    def showUser(self):
        print(f"User #{self.id} -> {self.name} ({self.email})")
        
    def getEmailDomain(self):
        reqEmail = self.email
        splittedEmail = reqEmail.split("@")
        print(splittedEmail[1])
        
        
        
if response.status_code == 200:
    data = response.json()
    # print(data)
    for i in data:
        id = i["id"] 
        name = i["name"] 
        email = i["email"] 
        users = jsonPlaceholderApi(id, name, email)
        # users.showUser()
        users.getEmailDomain()
        




