import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="expense_db"
)

cursor = db.cursor()
# cursor.execute(""" CREATE TABLE categories (
#     category_id INT PRIMARY KEY AUTO_INCREMENT,
#     category_name VARCHAR(50)
# )""")
# cursor.execute(""" CREATE TABLE expenses (
#     expense_id INT PRIMARY KEY AUTO_INCREMENT,
#     amount DECIMAL(10,2),
#     expense_date DATE,
#     category_id INT,
#     payment_method VARCHAR(30),
#     FOREIGN KEY (category_id) REFERENCES categories(category_id)
# )""")
# cursor.execute("""INSERT INTO categories (category_name)
# VALUES
# ('Food'),
# ('Travel'),
# ('Shopping'),
# ('Bills')""")
# db.commit()
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Add Category")
    print("3. View All Expenses")
    print("4. View Monthly Total")
    print("5. View Spending by Category")
    print("6. Exit")

    choice = input("Enter your choice: ")


   
    if choice == "1":

        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        category_id = int(input("Enter category ID: "))
        payment = input("Enter payment method: ")

        sql = """
        INSERT INTO expenses
        (amount, expense_date, category_id, payment_method)
        VALUES (%s, %s, %s, %s)"""
        values = (amount, date, category_id, payment)

        cursor.execute(sql, values)
        db.commit()

        print("Expense added successfully!")

    elif choice == "2":

        category = input("Enter category name: ")

        sql = "INSERT INTO categories (category_name) VALUES (%s)"

        cursor.execute(sql, (category,))
        db.commit()

        print("Category added successfully!")
    elif choice == "3":

        sql = """
        SELECT expenses.expense_id,
               expenses.amount,
               expenses.expense_date,
               categories.category_name,
               expenses.payment_method
        FROM expenses
        INNER JOIN categories
        ON expenses.category_id = categories.category_id
        """

        cursor.execute(sql)

        data = cursor.fetchall()

        for row in data:
            print(row)
    elif choice == "4":

        month = input("Enter month (YYYY-MM): ")

        sql = """
        SELECT SUM(amount)
        FROM expenses
        WHERE DATE_FORMAT(expense_date, '%Y-%m') = %s
        """

        cursor.execute(sql, (month,))

        total = cursor.fetchone()[0]

        if total:
            print("Total spending:", total)
        else:
            print("No expenses found")

    elif choice == "5":

        category = input("Enter category name: ")
        month = input("Enter month (YYYY-MM): ")

        sql = """
        SELECT SUM(expenses.amount)
        FROM expenses
        INNER JOIN categories
        ON expenses.category_id = categories.category_id
        WHERE categories.category_name = %s
        AND DATE_FORMAT(expenses.expense_date, '%Y-%m') = %s
        """

        cursor.execute(sql, (category, month))

        total = cursor.fetchone()[0]

        if total:
            print("Spending for", category, ":", total)
        else:
            print("No expenses found")
    elif choice == "6":

        print("Thank you!")
        break


    else:

        print("Invalid choice")