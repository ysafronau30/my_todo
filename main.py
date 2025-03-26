print('My To-Do list')


while True:
    command = input('Please enter add, show, edit, complete or exit: ').lower().strip()
    match command:
        case 'add':
            new_todo = input('Please enter new todo: ') + '\n'
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(new_todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            if len(todos) == 0:
                print('Todo list is empty. Please add a new todo.')
            else:
                for index, todo in enumerate(todos):
                    print(f'{index + 1}. {todo.capitalize()[:-1]}.')
        case 'edit':
            index_to_edit = int(input('Please enter todo\'s number in the list: ')) - 1
            new_todo = input('Enter a new todo: ') + '\n'
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos[index_to_edit] = new_todo
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            index_to_complete = int(input('Please enter todo\'s number in the list: '))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.pop(index_to_complete - 1)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'exit':
            break


print('Well done')