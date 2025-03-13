import mysql.connector

# connect กับ MySQL Container 
conn = mysql.connector.connect(
    host='my_mysql',
    user='Narawut.py',
    password='nnn.py',
    database='my_database'
)

# Create table user 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE
    )
""")
# info useer put in here!!

#cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Narawut", "narawut@gmail.com"))
#cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Thumsuan", "thumsuan@gmail.com"))
# วิธีนี้เรียกซ้ำหลายครั้ง = ช้า

data = [
    ("Narawut", "narawut@gmail.com"),
    ("Thumsuan", "thumsuan@gmail.com"),
    ("Nine", "nine@gmail.com"),
    ("JJ", "JJ@gmail.com")
]
cursor.executemany("INSERT INTO users (name, email) VALUES (%s, %s)", data)

# save ข้อมูล on datadase
conn.commit()
# แสดงผลข้อมูลทั้งหมด
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# ปิดการเชื่อมต่อ
cursor.close()
conn.close()