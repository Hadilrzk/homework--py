import random

FileName= "C:/Users/dell/Favorites/Documents/homework---py/to do list/tasks.csv"
def dict_to_list(task):
    return list(task.values())

def list_to_dict(data):
    return {
        'id': data[0],
        'name': data[1],
        'description': data[2],
        'status': data[3],
        'tag': data[4]
    }

def save_task(tasks_list, FileName):
    with open(FileName, 'w') as f:
        for task in tasks_list:
            line= ','.join(dict_to_list(task)) + '\n'
            f.write(line)

def read_task(FileName):
    tasks = []
    try:
        with open(FileName, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    task = list_to_dict(parts)
                    tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks





def add_Task(tasks_list):
    name= input('enter task name: ').strip()
    description = input('enter task description:')
    tag= input('enter tag(high/low), default:low:').strip().lower()
    if not tag:
        tag = 'low'
    status = 'new'    
    ID = str(random.randint(1000,9999))

    task = {
        'id':ID,
        'name': name,
        'description' : description,
        'status': status,
        'tag': tag
    }
    tasks_list.append(task)
    print(f"Task addedd successfuly")

def search_task(tasks_list, a):
    found = False
    for task in tasks_list:
        if task['id'] == a or task['name'].lower() == a:
          print('Task found')
          found = True
          break
    if not found:
        print(f'No task found with ID or name:{a}')

def delete_task(tasks_list, a):
    found = False
    for i, task in enumerate(tasks_list):
        if task['id']  == a or task['name'].lower() == a:
            delete = tasks_list.pop(i)
            print('Task deleted') 
            found = True
            break
    if not found:
        print(f'No task found with ID or name: {a}')

def update_status(tasks_list, a):
    found = False
    for task in tasks_list:
        if task['id'] == a or task['name'].lower() == a.lower():
            old_status = task['status']
            if old_status == "new":
                task['status'] = "completed"
            else:
                task['status'] = "new"
            
            print(f"Task '{task['name']}' (ID: {task['id']}) status updated from '{old_status}' to '{task['status']}'.")
            found = True
            break
    if not found:
        print(f"No task found with ID or Name: {a}")

def list_allTasks(tasks_list):
    if not tasks_list:
        print('No tasks found')
    else:
        print('______ALL TASKS____')
        for i, task in enumerate(tasks_list,1):
            print(f"{i}/ ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Status: {task['status']}, Tag: {task['tag']}")


def list_filtered(tasks_list):
    print('Filter option:')
    print('1/ Filter by tag')
    print('2/ Filter by status')
    print('3/Filter by both tag and status')

    filter_choice = input('enter your filter choice (1-3):')
    if filter_choice == "1":
        x = input('enter tag to filter by(high/low):').strip().lower()
        filtred_task = [task for task in tasks_list if task['tag'] == x]
        print(f'FILTRED TASKS : TAG ({x})')
        for i , task in enumerate(filtred_task,1):
            print(f"{i}/ ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Status: {task['status']}, Tag: {task['tag']}")

    elif filter_choice == "2":
        y = input('enter status to filter by(new/completed)')
        filtred_task = [task for task in tasks_list if task['status'] == y]
        print(f'FILTRED TASKS : STATUS {y}')
        for i, task in enumerate(filtred_task,1):
            print(f"{i}/ ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Status: {task['status']}, Tag: {task['tag']}")

    elif filter_choice == "3":
        tagF = input('enter tag(high/low):')
        statusF = input('enter status(new/completed):')
        filtred_task = [task for task in tasks_list if task['tag'] == tagF and task['status'] == statusF] 
        print('filtred task (tag', tagF,', status ',statusF,')')  
        for  task in filtred_task:
            print(f"{i}/ ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Status: {task['status']}, Tag: {task['tag']}")

    else:
        print('invalid choice')

def show_stat(tasks_list):
    total_tasks = len(tasks_list)
    new_tasks = len([task for task in tasks_list if task['status'] == "new"])
    comp_tasks = len([task for task in tasks_list if task['status'] == "completed"])
    high_tasks = len([task for task in tasks_list if task['tag'] == "high"])
    low_tasks = len([task for task in tasks_list if task['tag'] == "low"])
    
    print('_____TASK STATICS______')
    print('Total tasks is:',total_tasks)
    print('New tasks:',new_tasks)
    print('complted tasks:',comp_tasks)
    print('high priority tasks:',high_tasks)
    print('low priority tasks:',low_tasks)

def main():
    print('_____TO DO LIST_____')
    print('1/ add a new task')
    print('2/ search by id or name')
    print('3/ delete by id or name')
    print('4/ update status by id or name')
    print('5/list all tasks')
    print('6/list filtred')
    print('7/ show statics')
    print('q/ Quit')




 