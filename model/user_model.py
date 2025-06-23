import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.mysql import pymysql
import pymysql

app = Flask(__name__)

class user_model():
    def __init__(self):
        try:
            self.con = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="flask_tutorial",
                cursorclass=pymysql.cursors.DictCursor
            )
            # self.con.commit()
            self.cur = self.con.cursor()
            print("Connection successful ✅")
        except Exception as e:
            print("Connection failed ❌:", e)


    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        # print(result)

        if len(result)>0:
            return json.dumps(result)
        else:
            return "data is not present"


    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        self.con.commit()
        return  "user created successfully 1"


    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        print(data)
        self.con.commit()
        if self.cur.rowcount>0:
            return "user update successfully"
        else:
            return "nothing to update"

        # self.con.commit()


    def user_delete_model(self,id):
        self.cur.execute(f" DELETE FROM users WHERE id={id}")
        self.con.commit()
        return f"id number {id} delete successfully"