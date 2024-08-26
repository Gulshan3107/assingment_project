from flask import Flask,request,jsonify
import sqlite3


conn = sqlite3.connect("Users.db")
print("Database created successfully..!")

create_table ="create table if not exists users(id text, password text)"
conn.execute(create_table)
print("Table created Successfully..!")



#creating table for task--------------------------------------------------------------------------------------


create_table_for_task = "create table if not exists user_task12(task_id int,title text,description text,status text, priority text,due_date Date,id text)"
conn.execute(create_table_for_task)
print("Task table is created..!!")


app = Flask(__name__)


@app.route('/register',methods=['POST'])
def singup():
    user = request.get_json()
    conn = sqlite3.connect("Users.db")
    conn.execute("insert into users values (?,?)",(user['id'],user['password']))
    conn.commit()
    return "your account has been created"




@app.route("/login",methods=['POST'])
def login():
    user=request.get_json()
    conn=sqlite3.connect("Users.db")
    query=conn.execute("select * from users where id ='"+user['id']+"' and password='"+user['password']+"'")
    result_list=query.fetchone()
    print(result_list)
    conn.commit()
    return "login successfully"


#creating task fuction------------------------------------------------------------------------------------------------


@app.route('/create_task',methods=['POST'])
def create_task():
    user = request.get_json()
    conn = sqlite3.connect("Users.db")
    conn.execute("insert into user_task12 values (?,?,?,?,?,?,?)", (user['task_id'], user['title'],user['description'], user['status'],user['priority'],user['due_date'],user['id']))
    conn.commit()
    return "your Task has been created..!"




@app.route('/get_task',methods=['GET'])
def get_task():
    user = request.get_json()
    conn = sqlite3.connect("Users.db")
    query=conn.execute("select * from user_task12 left join users on user_task12.id= users.id ")
    result_list = query.fetchone()
    conn.commit()
    return "your task is Geting..!"


@app.route('/update_task',methods=['PUT'])
def update_task():
    user = request.get_json()
    conn = sqlite3.connect("Users.db")
    conn.execute("update user_task12 set description= '{}' where task_id = '{}'".format(user['description'],user['task_id']))
    conn.commit()
    return "Your Task title is Updated"




@app.route('/delete_task',methods=['DELETE'])
def delete_task():
    user = request.get_json()
    conn = sqlite3.connect("Users.db")
    conn.execute("delete from user_task12 where task_id='"+user['task_id']+"'")
    conn.commit()
    return "Your task is deleted"


app.run(port=5001)

