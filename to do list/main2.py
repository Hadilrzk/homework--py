import fct

tasks = []
def to_do_list():
    while True:
        fct.main()
        choice = input("Enter your choice (1-7, q): ").strip().lower()
        
        if choice == "q":
            break
        elif choice == "1":
            fct.add_Task(tasks)
        elif choice == "2":
            search_term = input("Enter task ID or Name to search: ").strip()
            fct.search_task(tasks, search_term)
        elif choice == "3":
            search_term = input("Enter task ID or Name to delete: ").strip()
            fct.delete_task(tasks, search_term)
        elif choice == "4":
            search_term = input("Enter task ID or Name: ").strip()
            fct.update_status(tasks, search_term)
        elif choice == "5":
            fct.list_allTasks(tasks)
        elif choice == "6":
            fct.list_filtered(tasks)
        elif choice == "7":
            fct.show_stat(tasks)
        else:
            print("Invalid choice. Please select 1-7 or 'q'.")

to_do_list()


       
    
