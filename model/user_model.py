import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.mysql import pymysql
import pymysql
from flask import make_response

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
            print("Connection successful ")
        except Exception as e:
            print("Connection failed :", e)


    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        # print(result)

        if len(result)>0:
            res=make_response({"payload":result},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
            # return json.dumps(result)
        else:
            return make_response({"message":"data is not present"},204)


    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        self.con.commit()
        return  make_response({"message":"user created successfully 1"},201)


    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        print(data)
        self.con.commit()
        if self.cur.rowcount>0:
            return make_response({"message":"user update successfully"},201)
        else:
            return make_response({"message":"nothing to update"},202)

        # self.con.commit()


    def user_delete_model(self,id):
        self.cur.execute(f" DELETE FROM users WHERE id={id}")
        self.con.commit()
        return make_response({"message":f"id number {id} delete successfully"},202)


    def user_patch_model(self,data,id):
        qry="UPDATE users SET "
        for key in data:
            qry=qry+f"{key}='{data[key]}',"

        qry=qry[:-1]+f" WHERE id={id}"

        self.cur.execute(qry)
        # print(data)
        self.con.commit()
        if self.cur.rowcount > 0:
            return make_response({"message": "user update successfully"}, 201)
        else:
            return make_response({"message": "nothing to update"}, 202)
        # return qry

    def user_pagination_model(self,limit,page):
        limit=int(limit)
        page=int(page)
        start=(page*limit)-limit
        qry=f"SELECT * FROM users LIMIT {start}, {limit}"

        self.cur.execute(qry)
        result = self.cur.fetchall()
        # print(result)

        if len(result) > 0:
            res = make_response({"payload": result , "limit":limit,"page_number":page  }, 200)
            return res
        else:
            return make_response({"message": "data is not present"}, 204)

    def user_upload_model(self,uid,filepath):
        self.cur.execute(f"UPDATE users SET avatar ='{filepath}' WHERE id={uid}")

        if self.cur.rowcount > 0:
            return make_response({"message": "File uploaded successfully"}, 201)
        else:
            return make_response({"message": "nothing to update"}, 202)

