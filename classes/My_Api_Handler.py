

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
            return response.json()['results'][0]
        print (f"{response.status_code} : {response.text}")
        