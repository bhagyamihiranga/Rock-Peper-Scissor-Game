import mysql.connector

def connection_dump():
    
    try:
            db = mysql.connector.connect(
            host = "localhost",
            user =  "root",
            password = "",
            database = "game_01",
        
        
            )
  
    except Exception as e:
        print(e)
    return db


