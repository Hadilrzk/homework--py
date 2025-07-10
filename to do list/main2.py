import fct
filename= "C:/Users/dell/Favorites/Documents/homework---py/to do list/tasks.csv"
def to_do_list():
    tasks = fct.read_task(filename)
    while True:
        fct.main()
        choice = input("Enter your choice (1-7, q): ").strip().lower()
        
        if choice == "q":
            fct.save_task(tasks, filename)
            break
        elif choice == "1":
            fct.add_Task(tasks)
            fct.save_task(tasks,filename)
        elif choice == "2":
            search_term = input("Enter task ID or Name to search: ").strip().lower()
            fct.search_task(tasks, search_term)
        elif choice == "3":
            search_term = input("Enter task ID or Name to delete: ").strip().lower()
            fct.delete_task(tasks, search_term)
            fct.save_task(tasks, filename)
        elif choice == "4":
            search_term = input("Enter task ID or Name: ").strip()
            fct.update_status(tasks, search_term)
            fct.save_task(tasks, filename)
        elif choice == "5":
            fct.list_allTasks(tasks)
        elif choice == "6":
            fct.list_filtered(tasks)
        elif choice == "7":
            fct.show_stat(tasks)
        else:
            print("Invalid choice. Please select 1-7 or 'q'.")

to_do_list()


       
    