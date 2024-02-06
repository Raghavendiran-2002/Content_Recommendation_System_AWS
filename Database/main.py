import csv
import mysql.connector as mysql
import os
from dotenv import load_dotenv
from pathlib import Path
DEPLOYMENT = "lcoal"


dotenv_path = Path('.env.local') if (
    DEPLOYMENT == "local") else Path('.env.prod'
                                     )
load_dotenv(dotenv_path=dotenv_path)

conn = mysql.connect(user=os.getenv('DBUSER'), password=os.getenv('DBPASS'), auth_plugin='mysql_native_password',
                     host=os.getenv('DBHOST'), database=os.getenv('DATABASE'))

cursor = conn.cursor()
createTB = "CREATE TABLE IF NOT EXISTS movie_recommendation(director_name LONGTEXT, actor_1_name LONGTEXT, actor_2_name LONGTEXT, actor_3_name LONGTEXT, genres LONGTEXT, movie_title LONGTEXT, comb LONGTEXT);"
cursor.execute(createTB)
conn.commit()
count = 1
with open('main_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    header = next(csv_reader)
    for row in csv_reader:
        sql = 'INSERT INTO movie_recommendation (director_name, actor_1_name, actor_2_name, actor_3_name,genres,movie_title,comb) VALUES ("{0}","{1}","{2}", "{3}","{4}", "{5}","{6}");'.format(
            str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]))
        cursor.execute(sql)
        conn.commit()
        print("Record inserted {}".format(count))
        count += 1


conn.commit()
cursor.close()
