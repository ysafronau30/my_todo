import functions
from functions import get_todos, write_todos

print('My To-Do list')


while True:
    command = input('Please enter add, show, edit, complete or exit: ').lower().strip()
    match command:
        case 'add':
            new_todo = input('Please enter new todo: ') + '\n'
            todos = get_todos()
            todos.append(new_todo)
            write_todos(todos)
        case 'show':
            todos = get_todos()
            if len(todos) == 0:
                print('Todo list is empty. Please add a new todo.')
            else:
                for index, todo in enumerate(todos):
                    print(f'{index + 1}. {todo.capitalize()[:-1]}')
        case 'edit':
            try:
                index_to_edit = int(input('Please enter todo\'s number in the list: ')) - 1
                todos = get_todos()
                if todos[index_to_edit]:
                    new_todo = input('Enter a new todo: ') + '\n'
                    todos[index_to_edit] = new_todo
                write_todos(todos)
            except IndexError:
                print('Please enter the right number!')
        case 'complete':
            try:
                index_to_complete = int(input('Please enter todo\'s number in the list: '))
                todos = get_todos()
                todos.pop(index_to_complete - 1)
                write_todos(todos)
            except IndexError:
                input('Please enter the right number!')
        case 'exit':
            print('Session has closed. See you later.')
            break
        case _ :
            print("Invalid command, please enter the right command!")