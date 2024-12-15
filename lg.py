import logging
import socket
import connection as conn 
db = conn.connection_dump()
cursor_object = db.cursor()

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

logging.basicConfig(filename="./logs/data.log",format="%(asctime)s %(message)s")

def log_data(level,msg):
     
     if level == "error" or level == "info" or level == "warning":
          
          cursor_object.execute("INSERT INTO logs (ip,status) VALUES (%s,%s)",(ip_address,f"{level} : {msg}"))
          db.commit()
          
          return True
         
     else:
         print('enter correct level to log data')     
         return False
    
     
     
     