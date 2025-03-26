print('My To-Do list')
todos = []

while True:
    command = input('Please enter add, show, edit, complete or exit: ').lower().strip()
    match command:
        case 'add':
            new_todo = input('Please enter new todo: ')
            todos.append(new_todo)
        case 'show':
            if len(todos) == 0:
                print('Todo list is empty. Please add a new todo.')
            else:
                for index, todo in enumerate(todos):
                    print(f'{index + 1}. {todo.capitalize()}.')
        case 'edit':
            index_to_edit = int(input('Please enter todo\'s number in the list: '))
            new_todo = input('Enter a new todo: ')
            todos[index_to_edit - 1] = new_todo
        case 'complete':
            index_to_complete = int(input('Please enter todo\'s number in the list: '))
            todos.pop(index_to_complete - 1)
        case 'exit':
            break


print('Well done')