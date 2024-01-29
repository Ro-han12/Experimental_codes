import mysql.connector



# print(con)
class DBHelper:
    def  __init__(self):
        self.con = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='rohan2939',
    database='python_test')
        query = 'CREATE TABLE IF NOT EXISTS user (userId INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(200), phone VARCHAR(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print('created')
    
    def insert_user(self,userid,username,phone):
        query = "INSERT INTO user(userId, username, phone) VALUES (1452, 'julie', '23356')"


        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('inserted')



helper=DBHelper()
helper.insert_user(1452, "julie", "23356")

