import pandas as pd
import requests
import time
import json
import urllib.parse

import database

# to store english words in array
english_words = pd.read_csv('english.txt',sep='\n',header=None)[0].tolist()
# test = (english_words)
test = (english_words[12000:12500])

word_counter = 0
word_properties = []
joinedStr = ""
joinedPartOfSpeech, joinedPhonetics, joinedDefinition, joinedExample, joinedSynonyms, joinedAntonyms = ("" for i in range(6))
phonetics_text, partOfSpeech = ([] for i in range(2))
definition, example, synonyms, antonyms = ([] for i in range(4))


def manageParams(properties, max):
    if(len(properties) != max):
        count = max - len(properties) 
        while count > 0 :
            properties.append("")
            count -= 1

def joinProperties(properties):
    if(len(properties) != 0):
        if(type(properties[0]) == list):
            joinedStr = tuple(properties[0])
            joinedStr = "|".join(joinedStr)
        else:
            joinedStr = tuple(properties)
            joinedStr = "|".join(joinedStr)
    else:
        joinedStr = ""
    return joinedStr

# to fetch the data from API
for word in test: 
    word_counter += 1
    word = urllib.parse.quote(word, safe='')

    URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    response = requests.get(url = URL)  
    time.sleep(3)  
    data = response.json()    
     
    for key in data[0].keys():                   
        if(key == "word" or key == "phonetic" or key == "origin"):            
            if(data[0][key] == []):
                word_properties.append("")
            else:
                word_properties.append(data[0][key])   
    
    manageParams(word_properties, 3)

    for key in data[0]["meanings"]:
        for keys in key.keys():
            if isinstance(key[keys], dict)== False:
                if(keys == "partOfSpeech"):
                    if(key[keys] == []):
                        partOfSpeech.append("")
                    else:
                        partOfSpeech.append(key[keys])
    
    joinedPartOfSpeech = joinProperties(partOfSpeech)
                
    for key in data[0]["phonetics"]:
        for keys in key.keys():
            if isinstance(key[keys], dict)== False:  
                if(keys == "text"):
                    phonetics_text.append(key[keys])                        
    #               print(keys, key[keys])  

    joinedPhonetics = joinProperties(phonetics_text)

    for key in data[0]["meanings"][0]["definitions"]:
        for keys in key.keys():
            if isinstance(key[keys], dict)== False:                
                if(keys == "definition"):
                    if(key[keys] != []):
                        definition.append(key[keys])
                elif(keys == "example"): 
                    if(key[keys] != []):
                        example.append(key[keys])
                elif(keys == "synonyms"): 
                    if(key[keys] != []):
                        synonyms.append(key[keys])
                elif(keys == "antonyms"): 
                    if(key[keys] != []):
                        antonyms.append(key[keys])
                    # print(key[keys])  
    
    joinedDefinition = joinProperties(definition)
    joinedExample = joinProperties(example)
    joinedSynonyms = joinProperties(synonyms)
    joinedAntonyms = joinProperties(antonyms)

    # print("word_properties=>>>", word_properties)  
    # print("joinedPartOfSpeech=>>>", joinedPartOfSpeech)   
    # print("joinedPhonetics=>>>",joinedPhonetics)
    # print("Defini=>>>", joinedDefinition)
    # print("exa=>>>", joinedExample)
    # print("sys=>>>", joinedSynonyms)
    # print("anto=>>>", joinedAntonyms)

    database.Insert_WordProperties(word_properties, joinedPartOfSpeech, joinedPhonetics, joinedDefinition, joinedExample, joinedSynonyms, joinedAntonyms) 

    print(word_counter, "Record Inserted!")

    word_properties.clear()
    partOfSpeech.clear()
    phonetics_text.clear()
    definition.clear()
    example.clear()
    synonyms.clear()
    antonyms.clear()