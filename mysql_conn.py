import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test_db"
)
cursor = conn.cursor()
#cursor.execute(""" CREATE TABLE tb_student(id INT,name VARCHAR(50),age INT)""")
#cursor.execute("INSERT INTO tb_student VALUES(%s,%s,%s)",(1,"sheri",22))
#cursor.execute("""INSERT INTO tb_student VALUES(2,"anu",21)""")
#conn.commit()
#cursor.execute("SELECT * FROM tb_student")
#for row in cursor.fetchall():
    #print(row)
#conn.close()
#cursor.execute("""UPDATE tb_student set name="rahul" where id=2""")
#conn.commit()
cursor.execute("""DELETE FROM tb_student WHERE id=2""")
cursor.execute("SELECT * FROM tb_student")
for row in cursor.fetchall():
    print(row)
conn.close()