<<<<<<< HEAD
# import mysql.connector
# import os

# # ดึงตัวแปร env จาก docker-compose.yml
# host = os.getenv('MYSQL_HOST', 'localhost')
# user = os.getenv('MYSQL_USER', 'root')
# password = os.getenv('MYSQL_PASSWORD', 'root')
# database = os.getenv('MYSQL_DB', 'sales_db')

# # เชื่อมต่อ MySQL
# try:
#     conn = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )
#     print("✅ Connected to MySQL database!")
# except mysql.connector.Error as err:
#     print(f"❌ Error: {err}")
#---> จำลอง และ setting docker


=======
>>>>>>> d216e9f (Reinitialize Git in the correct directory)
import pandas as pd
import mysql.connector
import os

# Extract: ดึงข้อมูลจากไฟล์ CSV
def extract(csv_file):
    print(f"Extracting data from {csv_file}")
    data = pd.read_csv(csv_file)
    return data

# Transform: แปลงข้อมูลให้อยู่ในรูปแบบที่ต้องการ
def transform(data):
    print("Transforming data...")
    data['sale_date'] = pd.to_datetime(data['sale_date'])
    data['total_price'] = data['price'] * data['quantity']
    return data

# Load: โหลดข้อมูลเข้า MySQL
def load(data, db_config):
    print("Loading data into MySQL...")
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    for _, row in data.iterrows():
        cursor.execute('''
        INSERT INTO sales (product_name, price, quantity, sale_date, total_price)
        VALUES (%s, %s, %s, %s, %s)
        ''', (row['product_name'], row['price'], row['quantity'], row['sale_date'], row['total_price']))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data successfully loaded!")

# Config การเชื่อมต่อ MySQL
db_config = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'user'),
    'password': os.getenv('MYSQL_PASSWORD', 'password'),
    'database': os.getenv('MYSQL_DB', 'sales_db')
}

# ไฟล์ CSV ที่ใช้
csv_file = 'data/sales_data.csv'

# ETL Pipeline
if __name__ == "__main__":
    data = extract(csv_file)
    transformed_data = transform(data)
<<<<<<< HEAD
    load(transformed_data, db_config)
=======
    load(transformed_data, db_config)
>>>>>>> d216e9f (Reinitialize Git in the correct directory)
