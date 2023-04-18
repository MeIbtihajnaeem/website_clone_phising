import resources
from bs4 import BeautifulSoup

class WebsiteBuilder:
    def build(redirectRequest):
        filePath = resources.PathFinder("index.html").find()
        print(filePath)
        output=""
        with open('../project/'+filePath, 'r') as file :
            filedata = file.read()
        soup = BeautifulSoup(filedata, "html.parser")
        forms = soup.find_all("form")
        for form in forms:
            current_action = form.get("action")
            form["action"] = redirectRequest
            
        with open("../project/"+filePath, 'w') as file:
            file.write(str(soup))
            file.close()  
  