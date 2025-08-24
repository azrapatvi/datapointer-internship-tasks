import csv
from datetime import datetime
import os

while True:
    print()
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Filter Expense")
    print("4. Delete Expense")
    print("5. Monthly Summary")
    print("6. Exit")
    choice=int(input("Enter choice (1-6): "))
    print()

    if os.path.exists('expenses.csv'):
        pass
    else:
        with open('expenses.csv', 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])

    match choice:
        case 1:
            date= input("Enter date (DD-MM-YYYY): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")

            with open('expenses.csv','a',newline='')as f:
                writer=csv.writer(f)
                writer.writerow([date, amount, category, description])
            print("expense added successfully!\n")
        
        case 2:
            with open('expenses.csv','r')as f:
                print(f.read())
                print()
        
        case 3:
            filter_choice = int(input("Filter by (1) Date (2) Category: "))

            match filter_choice:
                case 1:
                    search_by_date=input("enter date to filter(DD-MM-YYYY)")
                    with open('expenses.csv','r')as f:
                        reader=csv.reader(f)
                        next(reader)#skips the header
                        for row in reader:
                            if row[0].strip().lower()==search_by_date.strip().lower():
                                print(row)
                    print()
                case 2:
                    search_by_category = input("Enter category to filter: ")
                    with open('expenses.csv','r')as f:
                        reader=csv.reader(f)
                        next(reader)
                        for row in reader:
                            if row[2].strip().lower()==search_by_category.strip().lower():
                                print(row)
                    print()
                case _:
                    print("invalid choice")
                    continue
        case 4:
            print("1. Delete by Date")
            print("2. Delete by Category")
            delete_choice = int(input("Enter choice (1-2): "))

            match delete_choice:
                case 1:
                    delete_by_date = input("Enter date to delete (DD-MM-YYYY): ")
                    rows = []
                    with open('expenses.csv', 'r') as f:
                        reader = csv.reader(f)
                        header = next(reader)
                        for row in reader:
                            if row[0].strip() != delete_by_date.strip():
                                rows.append(row)
                    with open('expenses.csv', 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)         # write header back
                        writer.writerows(rows)
                    print("Expense(s) deleted successfully by date!\n")

                case 2:
                    delete_by_category = input("Enter the category to delete: ")
                    rows = []
                    with open('expenses.csv', 'r') as f:
                        reader = csv.reader(f)
                        header = next(reader)
                        for row in reader:
                            if row[2].strip().lower() != delete_by_category.strip().lower():
                                rows.append(row)
                    with open('expenses.csv', 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(header)         # write header back
                        writer.writerows(rows)
                    print("Expense(s) deleted successfully by category!\n")

                case _:
                    print("Enter a valid choice\n")

        case 5:
            summary_by_month=input("enter month whose summary you want(MM-YYYY):")
            total=0
            with open('expenses.csv','r')as f:
                reader=csv.reader(f)
                header=next(reader)

                for row in reader:
                    date_obj=datetime.strptime(row[0],"%d-%m-%Y")
                    month_year=date_obj.strftime("%m-%Y")

                    if month_year==summary_by_month:
                        total+=float(row[1])#because the amount which is stored here is in the form of string 
            
            print(f"Total Expense in {summary_by_month}: ₹{total:.2f}")
            print()

        case 6:
            print("exiting the program")
            break

        case _:
            print("invalid choice!")



