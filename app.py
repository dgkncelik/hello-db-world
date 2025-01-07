import redis
from pymongo import MongoClient
import mysql.connector

def write_to_redis():
    r = redis.Redis(host='redis_container', port=6379)
    r.set('message', 'Hello, Redis!')
    print('Redis:', r.get('message').decode('utf-8'))

def write_to_mongo():
    client = MongoClient('mongo_container', 27017)
    db = client.test_db
    db.test_collection.insert_one({'message': 'Hello, MongoDB!'})
    message = db.test_collection.find_one({'message': 'Hello, MongoDB!'})
    print('MongoDB:', message['message'])

def write_to_mysql():
    conn = mysql.connector.connect(
        host='mysql_container',
        user='user',
        password='password',
        database='test_db'
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255))")
    cursor.execute("INSERT INTO messages (message) VALUES ('Hello, MySQL!')")
    conn.commit()
    cursor.execute("SELECT message FROM messages")
    for row in cursor.fetchall():
        print('MySQL:', row[0])
    cursor.close()
    conn.close()

if __name__ == "__main__":
    write_to_redis()
    write_to_mongo()
    write_to_mysql()
