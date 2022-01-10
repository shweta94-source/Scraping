import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kalash",
  database="scrap"
)

mycursor = mydb.cursor()

def Insert_WordProperties(properties, partOfSpeech):
  values = []
  sql ="INSERT INTO `scrap`.`words` (`WORD`, `PHONETIC`, `ORIGIN`, `PARTOFSPEECH`) VALUES (%s, %s, %s, %s)"
  for k in properties:
    values.append(k)

  if(len(values) != 3):
    # print(values)
    # print(len(values))
    count = 3 - len(values) 
    while count > 0 :
      # print(count)
      values.append("")
      count -= 1

  values.append(partOfSpeech)
  val  = tuple(values)
  mycursor.execute(sql, val)
  mydb.commit()


def Insert_Phonetics(word_counter, phonetics_text, phonetics_audio):
  if(len(phonetics_text) != 0 and len(phonetics_audio) != 0):   
        for text in phonetics_text:
          for audio in phonetics_audio:
            sql = "INSERT INTO `scrap`.`phonetics`(`WORD_ID`,`PHONETICS_TEXT`,`PHONETICS_AUDIO`) VALUES(%s, %s, %s)"
            val = (word_counter, text, audio)
            mycursor.execute(sql, val)
            mydb.commit()



def Insert_Definition(word_counter, definition, example, synonyms, antonyms): 
  for k in range(len(definition)):
    if (len(example) <= k ):
      example.insert(k, "")
    if (len(synonyms) <= k ):
      synonyms.insert(k, "")
    if (len(antonyms) <= k ):
      antonyms.insert(k, "")
    sql = "INSERT INTO `scrap`.`definations`(`WORD_ID`,`DEFINATION`,`EXAMPLE`,`SYNONYMS`,`ANTONYMS`)VALUES(%s, %s, %s, %s, %s)"
    val = (word_counter, definition[k], example[k], synonyms[k], antonyms[k])
    mycursor.execute(sql, val)
    mydb.commit()
    




