import csv
import os

while True:
    print()
    print("--- TODO LIST ---")
    print("1. Add Task")
    print("2. View Tasks") #read tasks
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice=int(input("enter choice(1-5):"))
    srno=0
    print()

    if os.path.exists('tasks.csv'):
        pass
    else:
        with open('tasks.csv','w',newline='')as f:
            writer=csv.writer(f)
            writer.writerow(['srno','Task','Status'])
    match choice:
        
        case 1:
            new_task = input("Enter new task: ")

            # Find the last srno
            srno = 0
            with open('tasks.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                for row in reader:
                    srno = int(row[0])
                srno += 1

            with open('tasks.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([srno, new_task, 'Incomplete'])

            print("Task added successfully!\n")

        
        case 2:
            with open('tasks.csv','r')as f:
                tasks=f.read()
                print(tasks)
                print()

        case 3:
            no_of_task_to_complete=input("Enter the no of task to mark as complete: ")
            rows=[]
            with open('tasks.csv','r')as f:
                reader=csv.reader(f)
                for row in reader:
                    if row[0]==no_of_task_to_complete and row[2]=='Incomplete':
                        row[2]='Complete'
                    rows.append(row)
            with open('tasks.csv','w',newline='')as f:
                writer=csv.writer(f)
                writer.writerows(rows)
            print("Task marked as complete!")
            print()

        case 4:
            no_of_task_to_delete=input("Enter the no of task to be deleted: ")
            rows=[]
            with open('tasks.csv','r')as f:
                reader=csv.reader(f)
                for row in reader:
                    if row[0]!=no_of_task_to_delete:
                        rows.append(row)
            with open('tasks.csv','w',newline='')as f:
                writer=csv.writer(f)
                writer.writerows(rows)
            print("Task deleted successfully!")
            print()
        case 5:
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")
                