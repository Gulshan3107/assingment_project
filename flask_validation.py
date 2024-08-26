import sqlite3

con=sqlite3.connect("Users.db")

query_result=con.execute("Select * from users")

for x in query_result:
    print("id:", x[0])
    print("password :",x[1])
    # print("task_id :",x[0])
    # print("title :",x[1])
    # print("description :", x[2])
    # print("status :", x[3])
    # print("priority :", x[4])
    # print("due_date :", x[5])
    # print("user_id :", x[6])