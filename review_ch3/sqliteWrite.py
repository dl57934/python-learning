import sqlite3

#따로 파일은 안만들어 줘도 됩니다. 자동 생성
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()

#여러 줄 실행 가능
cur.executescript("""
/*fruits테이블 있다면 삭제*/ 
DROP TABLE IF EXISTS fruits;

/*PRIMARY KEY 중복 안되고 NULL값이면 안된다 */
/*UNIQUE 중복 안되고 NULL 값 허용한다. */
CREATE TABLE fruits(id INTEGER PRIMARY KEY,
 name STRING UNIQUE,
 PRICE INTEGER);

INSERT INTO fruits(name,price) VALUES("오렌지",3000);
INSERT INTO fruits(name,price) VALUES("사과",5000);
INSERT INTO fruits(name,price) VALUES("바나나",7000);


""")
#코드 실행
conn.commit()
cur = conn.cursor()
# 찾기
cur.execute("SELECT id, name, price  FROM fruits;")
item_list = cur.fetchall()
for item in item_list:
    print(item) 

