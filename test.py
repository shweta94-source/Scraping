import pandas as pd
import requests
import time
import json

import data_tables
import database

# to store english words in array
english_words = pd.read_csv('english.txt',sep='\n',header=None)[0].tolist()
# test = (english_words)
test = (english_words[:30])

word_counter = 0
word_properties = []
partOfSpeech = ""
phonetics_text, phonetics_audio = ([] for i in range(2))
definition, example, synonyms, antonyms = ([] for i in range(4))

# to fetch the data from API
for word in test: 
    word_counter += 1
    URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    print("\n"+URL)    
    response = requests.get(url = URL)  
    time.sleep(3)  
    data = response.json()  
    # print((data[0]))
     
    for key in data[0].keys():                   
        if(key == "word" or key == "phonetic" or key == "origin"):            
            if(data[0][key] == []):
                word_properties.append("")
            else:
                word_properties.append(data[0][key])   

    for key in data[0]["meanings"]:
        for keys in key.keys():
            if isinstance(key[keys], dict)== False:
                if(keys == "partOfSpeech"):
                    if(key[keys] == []):
                        partOfSpeech =""
                    else:
                        partOfSpeech = key[keys]
                
    #                print(keys, key[keys])

    for key in data[0]["phonetics"]:
        for keys in key.keys():
            if isinstance(key[keys], dict)== False:  
                if(keys == "text"):
                    phonetics_text.append(key[keys])
                elif(keys == "audio"):
                    phonetics_audio.append(key[keys])
    #             print(keys, key[keys])  

    for key in data[0]["meanings"][0]["definitions"]:
        for keys in key.keys():
            if isinstance(key[keys], dict)== False:                
                if(keys == "definition"):
                    if(key[keys] == []):
                        definition.append("")
                    else:
                        definition.append(key[keys])
                elif(keys == "example"): 
                    if(key[keys] == []):
                        example.append("")
                    else:
                        example.append(key[keys])
                elif(keys == "synonyms"): 
                    if(key[keys] == []):
                        synonyms.append("")
                    else:
                        synonyms.append(key[keys])
                elif(keys == "antonyms"): 
                    if(key[keys] == []):
                        antonyms.append("")
                    else:
                        antonyms.append(key[keys])
                    # print(key[keys])  
        

    # print(word_properties)   
    # print(phonetics_text, phonetics_audio)
    # print(definition, example, synonyms, antonyms)

    database.Insert_WordProperties(word_properties, partOfSpeech) 
    database.Insert_Phonetics(word_counter, phonetics_text, phonetics_audio)    
    database.Insert_Definition(word_counter, definition, example, synonyms, antonyms)       

    print(word_counter, "Record Inserted!")

    word_properties.clear()
    phonetics_text.clear()
    phonetics_audio.clear()
    definition.clear()
    example.clear()
    synonyms.clear()
    antonyms.clear()