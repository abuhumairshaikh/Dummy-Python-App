import mysql.connector

# RDS connection details
db = mysql.connector.connect(
    host="YOUR_RDS_ENDPOINT",
    user="admin",
    password="YOUR_PASSWORD",
    database="myappdb"
)

cursor = db.cursor()

def insert_user():
    name = input("Enter name: ")
    email = input("Enter email: ")

    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)

    cursor.execute(sql, values)
    db.commit()

    print("✅ User inserted successfully!")

def show_users():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    print("\n--- Users in Database ---")
    for row in result:
        print(row)

while True:
    print("\n1. Insert User")
    print("2. Show Users")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        insert_user()
    elif choice == "2":
        show_users()
    elif choice == "3":
        break
    else:
        print("Invalid option")

cursor.close()
db.close()
