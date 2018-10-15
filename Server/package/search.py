import requests

SEARCH_URL = "https://www.googleapis.com/customsearch/v1?"

class google_search_engineering():

    def __init__(self, API_key, engineering_ID):
        self.API_key = API_key
        self.engineering_ID = engineering_ID

    def searching(self, keyword):
        params = {"key":self.API_key,"cx":self.engineering_ID,"q":keyword}
        reponse = requests.get(SEARCH_URL, params=params)
        return reponse.text

if __name__ == "__main__":

    search = google_search_engineering(open("../key/api_key.txt").read(), "015664378164063206829:iu-niupqc9i")
    print(search.searching("けっしょうばん"))