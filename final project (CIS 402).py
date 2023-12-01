import mysql.connector as mc

conn = mc.connect(
    host='BATTLESTATION', # name of my PC
    user='root',
    password='NOTmeNOT@2002',
    database='menagerie'
)

c = conn.cursor()

def show_databases():
    c.execute("SHOW DATABASES")
    databases = c.fetchall()
    for database in databases:
        print(database)

def main():
    show_databases()

main()