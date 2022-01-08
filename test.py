import pandas as pd
import requests
import time

# to store english words in array
english_words = pd.read_csv('english.txt',sep='\n',header=None)[0].tolist()
test = (english_words)
# test = (english_words[:15])


# to fetch the data from API
for word in test:   
    URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    print("\n"+URL)    
    response = requests.get(url = URL)  
    time.sleep(3)  

    data = response.json()  
    # print(type((data[0])))
    print(data[0]["word"])