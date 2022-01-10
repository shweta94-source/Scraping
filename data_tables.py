import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kalash",
  database="scrap"
)

mycursor = mydb.cursor()

mycursor.execute ("CREATE TABLE `scrap`.`words` ("+
                  "`ID` int NOT NULL AUTO_INCREMENT,"+
                  "`WORD` varchar(255) DEFAULT NULL,"+
                  "`PHONETIC` varchar(255) DEFAULT NULL,"+
                  "`ORIGIN` varchar(255) DEFAULT NULL,"+
                  "`PARTOFSPEECH` varchar(255) DEFAULT NULL,"+
                  "PRIMARY KEY (`ID`))")

mycursor.execute("CREATE TABLE `scrap`.`phonetics` ("+
                  "`ID` INT NOT NULL AUTO_INCREMENT,"+
                  "`WORD_ID` VARCHAR(45) NULL,"+
                  "`PHONETICS_TEXT` VARCHAR(255) NULL,"+
                  "`PHONETICS_AUDIO` VARCHAR(255) NULL,"+
                  "PRIMARY KEY (`ID`)) ")

mycursor.execute("CREATE TABLE `scrap`.`definations` ("+
                  "`ID` INT NOT NULL AUTO_INCREMENT,"+
                  "`WORD_ID` VARCHAR(45) NULL,"+
                  "`DEFINATION` VARCHAR(255) NULL,"+
                  "`EXAMPLE` VARCHAR(255) NULL,"+
                  "`SYNONYMS` VARCHAR(255) NULL,"+
                  "`ANTONYMS` VARCHAR(255) NULL,"+
                  "PRIMARY KEY (`ID`))")