import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kalash",
  database="scrap"
)

mycursor = mydb.cursor()


mycursor.execute ("CREATE TABLE `scrap`.`words` ("+
                  "`ID` INT NOT NULL AUTO_INCREMENT,"+
                  "`WORD` VARCHAR(999) NULL,"+
                  "`PHONETIC` VARCHAR(999) NULL,"+
                  "`PHONETICS_TEXT` VARCHAR(999) NULL,"+
                  "`ORIGIN` VARCHAR(999) NULL,"+
                  "`PARTOFSPEECH` VARCHAR(999) NULL,"+
                  "`DEFINITION` VARCHAR(999) NULL,"+
                  "`EXAMPLE` VARCHAR(999) NULL,"+
                  "`SYNONYMS` VARCHAR(999) NULL,"+
                  "`ANTONYMS` VARCHAR(999) NULL,"+
                  "PRIMARY KEY (`ID`))")

def Insert_WordProperties(word_properties, joinedPartOfSpeech, joinedPhonetics, joinedDefinition, joinedExample, joinedSynonyms, joinedAntonyms):
  sql = " INSERT INTO `scrap`.`words`(`WORD`,`PHONETIC`,`ORIGIN`,`PARTOFSPEECH`,`PHONETICS_TEXT`,`DEFINITION`,`EXAMPLE`,`SYNONYMS`,`ANTONYMS`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = (word_properties[0], word_properties[1], word_properties[2], joinedPartOfSpeech, joinedPhonetics, joinedDefinition, joinedExample, joinedSynonyms, joinedAntonyms)
  mycursor.execute(sql, val)
  mydb.commit()


