import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library"
)
cursor = db.cursor()
# cursor.execute("""CREATE TABLE books (
#     book_id INT PRIMARY KEY,
#     title VARCHAR(100),
#     author VARCHAR(100),
#     price DECIMAL(10,2)
# )""")
while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":
        id = int(input("Enter book id: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        price = int(input("Enter price: "))

        sql = "INSERT INTO books VALUES (%s, %s, %s, %s)"
        values = (id, title, author, price)

        cursor.execute(sql, values)
        db.commit()

        print("Book added successfully")

    # View Books
    elif choice == "2":
        cursor.execute("SELECT * FROM books")

        for book in cursor.fetchall():
            print(book)

    # Search Book
    elif choice == "3":
        id = int(input("Enter book id: "))

        sql = "SELECT * FROM books WHERE book_id = %s"
        cursor.execute(sql, (id,))

        book = cursor.fetchone()

        if book:
            print(book)
        else:
            print("Book not found")

    # Update Book
    elif choice == "4":
        id = int(input("Enter book id: "))
        price = int(input("Enter new price: "))

        sql = "UPDATE books SET price = %s WHERE book_id = %s"
        values = (price, id)

        cursor.execute(sql, values)
        db.commit()

        print("Book updated successfully")

    # Delete Book
    elif choice == "5":
        id = int(input("Enter book id: "))

        sql = "DELETE FROM books WHERE book_id = %s"
        cursor.execute(sql, (id,))
        db.commit()

        print("Book deleted successfully")

    # Exit
    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice")