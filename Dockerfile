# ใช้ Python เวอร์ชัน 3.9
FROM python:3.9-slim

# ตั้งค่า working directory ใน container
WORKDIR /app

# คัดลอกไฟล์ requirements.txt เข้า container
COPY requirements.txt requirements.txt

# ติดตั้ง dependencies
RUN pip install -r requirements.txt

# คัดลอกโค้ดทั้งหมดเข้า container
COPY . .

# รัน main.py เมื่อ container เริ่มทำงาน
CMD ["python", "main.py"]
