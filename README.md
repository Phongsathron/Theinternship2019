# The Internship 2019
## Hangman
เป็นเกมส์ทายคำตามหมวดหมู่ที่เลือก ซึ่งเกมส์จะสุ่มคำศัพท์ตามหมวดหมู่ที่ผุ้เล่นเลือก และให้คำใบ้เพื่อให้ผู้เล่นทายคำให้ถูกต้อง
### กฎในการเล่น
- ผู้เล่นสามารถใส่ตัวอักษรที่ต้องการทายได้เฉพาะตัวอักษรภาษาอังกฤษ (a-z A-Z) โดยตัวเกมส์เป็น case-insensitive
- เมื่อผู้เล่นทายตัวอักษรถูก ผู้เล่นจะได้คะแนน + 1 ตามจำนวนตัวอักษรที่ทายถูก เช่น คำศัพท์คำว่า `Coffee` หากผู้เล่นทายตัวอักษร `e` ผู้เล่นจะได้ 2 คะแนน เพราะคำว่า `Coffee` มีตัวอักษร `e` 2 ตัวอักษร
- ผู้เล่นมีสิทธิ์ทายคำศัพท์ผิดได้เพียง 10 ครั้งเท่านั้น
- หากคำศัพท์มีตัวอักษรที่เป็นช่องว่าง ตัวเลข อักขระพิเศษ ตัวเกมส์จะแสดงให้เลย

โดยตัวเกมส์เริ่มต้นนั้นจะมีอยู่ด้วยกัน 2 หมวดหมู่
- Animal ให้ทายว่าเสียงร้องของสัตว์นั้นคือสัตว์ชนิดใด
- BNK48 members ทายชื่อของเมมเบอร์ตามจุดเด่นต่างๆ

### สิ่งที่ตัวเกมส์ต้องการ
- Python 3.6 ขึ้นไป
### วิธีการเล่น
- เปิด Terminal แล้ว CD ไปที่ Directory ที่โหลดไฟล์ไว้
- ใช้คำสั่ง 
```bash
python hangman.py
```
### การเพิ่มหมวดหมู่และคำศัพท์ในเกมส์
ผู้เล่นสามารถเพิ่มหมวดหมู่ และคำศัพท์ได้ โดยตัวเกมส์นี้เก็บไฟล์คำศัพท์ต่างๆ ไว้ในโฟลเดอร์ `words` ผู้เล่นสามารถสร้างไฟล์คำศัพท์ใหม่ `.txt.` ได้ โดยชื่อไฟล์จะถูกนำไปเป็นชื่อหมวดหมู่ของคำศัพท์โดยอัตโนมัติ

#### รูปแบบ Format ของไฟล์คำศัพท์
ในไฟล์นี้จะประกอบไปด้วยคำศัพท์ และคำใบ้ โดยคำศัพท์จะอยู่ก่อนบรรทัดของคำใบ้ และคำใบ้จะต้องใส่สัญลักษณ์ `##` นำหน้าคำใบ้ด้วย ตัวอย่างเช่น

```
>> Animal.txt

Cat
##Meow Meow
Dog
##Hong Hong
Bird
##Jib Jib
Duck
##Kab Kab
Fox
##Ring-ding-ding-ding-dingeringeding!
```

## Weather (XML to JSON)
เป็นโปรแกรมสำหรับแปลงไฟล์ Format `XML` ให้มาเป็น Format `JSON`

### สิ่งที่โปรแกรมต้องการ
- Python 3.6 ขึ้นไป
- [xmltodict](https://github.com/martinblech/xmltodict)

### วิธีการติดตั้ง
- เปิด Terminal แล้ว CD ไปที่ Directory ที่โหลดไฟล์ไว้
- ใช้คำสั่ง
```
pip install -r requirements.txt
```
 
### วิธีการใช้งาน
- เปิด Terminal แล้ว CD ไปที่ Directory ที่โหลดไฟล์ไว้
- ใช้คำสั่ง
```
python weather.py [ชื่อไฟล์ Format XML] [ชื่อไฟล์ Format JSON ที่ต้องการ]
```
