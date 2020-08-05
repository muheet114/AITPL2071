import sqlite3 as lite
import string as long

class StudentDatabase(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('institute.db')
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS student(studentId INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR,"
                    "course VARCHAR,phone NUMBER(10),email VARCHAR ) "
                )
        except Exception:
            print("Unable to create a DB")

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO student(name, course, phone, email) VALUES(?,?,?,?)", data)
                return True
        except Exception:
            return False

    def veiw_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM student")
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self, Id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM student WHERE studentId = ?"
                cur.execute(sql, [Id])
                return True
        except Exception:
            return False

    def update_data(self, name, id):
        try:
            with con:
                cur = con.cursor
                sql = '''UPDATE student set name VALUE = (?) WHERE studentId = ?'''
                cur.execute(sql, name, [id])
                return True
        except Exception:
            return False


def main():
    print("*" * 40)
    print("\n :: INSTITUTE MANAGEMENT ::")
    print("*" * 40)
    print("\n")
    db = StudentDatabase()
    print("*" * 40)
    print("\n 1. Insert Student")
    print("\n 2. View Student")
    print("\n 3. Delete Student")
    print("\n 4. Update Student")
    print("*" * 40)

    choice = input("Enter you choice : ")
    if choice == "1":
        name = input("\nEnter the Student Name : ")
        course = input("\nEnter the Student Course : ")
        phone = input("\nEnter the Student Phone Number : ")
        email = input("\nEnter the Student Email : ")
        if db.insert_data([name, course, phone, email]):
            print("\nStudent data inserted Successfully !")
        else:
            print("OOPS SOMETHING WENT WRONG !!")

    elif choice == "2":
        print("\n :: Student List ")
        for index, item in enumerate(db.veiw_data()):
            print("\n Sl no : " + str(index + 1))
            print("\n Student Id :" + str(item[0]))
            print("\n Name :" + str(item[1]))
            print("\n Course :" + str(item[2]))
            print("\n Phone :" + str(item[3]))
            print("\n Email :" + str(item[4]))

    elif choice == "3":
        record_id = input("Enter the Student Id : ")
        if db.delete_data(record_id):
            print("Course was deleted successfully ")
        else:
            print("OOPS SOMETHING WENT WRONG ")

    elif choice == "4":
        record = input("Enter the Student Id : ")
        name = input("Enter the Student Name correctly : ")
        if db.update_data(name, record):
            print("\nStudent data updated Successfully !")
        else:
            print("OOPS SOMETHING WENT WRONG !!")
    else:
        print("BAD CHOICE !")


if __name__ == '__main__':
    main()
