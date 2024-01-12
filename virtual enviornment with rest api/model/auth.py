import mysql.connector
import json
from flask import make_response
from datetime import datetime

class auth():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="",database="test_python_api")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True) 
            print("connection established -> database connected")
        except:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX <- connection error -> XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            
    def getdata(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
            res=make_response({"payload":result},201)
            res.headers["Access-Control-Allow-Origin"]="*"
            return res
            # return json.dumps(result)
        else:
            return make_response({"msg":"data not found"})
                
    

    def signup(self, request):
        try:
            print('ok')

            # Decode the byte string into a regular string
            json_string = request.data.decode('utf-8')

            # Parse the string as JSON
            json_data = json.loads(json_string)

            # Print the "name" field
            name = json_data.get('name')
            print(name)

            # Use a parameterized query to insert data into the database
            query = "INSERT INTO users (name) VALUES (%s)"
            self.cur.execute(query, (name,))

            return {"msg": "User successfully created"}, 201
        except Exception as e:
            return {"error": str(e)}, 400


        
    def upload(self, request):
        try:
            # Accessing the uploaded file from the request
            file = request.files['image']        
            new_filename =  str(datetime.now().timestamp()).replace(".", "") # Generating unique name for the file
            split_filename = file.filename.split(".") # Spliting ORIGINAL filename to seperate extenstion
            ext_pos = len(split_filename)-1 # Canlculating last index of the list got by splitting the filname
            ext = split_filename[ext_pos] # Using last index to get the file extension

            print(split_filename,ext_pos,ext)
            file.save(f"uploads/{new_filename}.{ext}")            
            # Returning a success response
            return make_response({"msg": "File successfully Uploaded"}, 201)
        
        except Exception as e:
            # Handling exceptions and returning an error response
            return make_response({"error": str(e)}, 400)



       