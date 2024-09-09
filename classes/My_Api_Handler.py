

class My_Api_Handler():

    def __init__(self):
        pass

    def get_cat_fact(self):
        cat_url = "https://catfact.ninja/fact"
        response = requests.get(url=cat_url, timeout=10)

        if response.status_code == 200:
            return response.text
        print (f"{response.status_code} : {response.text}")
        return ""

    def get_user(self):
        api_url = "https://randomuser.me/api/"
        response = requests.get(url=api_url, timeout=10)
        if response.status_code == 200:
            response.json()['results'][0]
        print (f"{response.status_code} : {response.text}")
        
    def get_yes_no(self):
        """Function should make a get request to https://yesno.wtf/api and return the answer.  This api returns as yes or no value.  The response
        will be a json object if the status code is 200.  Where the value of the answer is in the ['answer'] key of the json object"""


