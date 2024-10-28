def save_tasks(tasks, filename="tasks.txt"):
    # Открываем файл в режиме записи ('w').
    # Если файл уже существует, он перезапишется.
    with open(filename, 'w') as file:
        # Перебираем список задач и записываем каждую задачу в новую строку.
        for task in tasks:
            file.write(task + '\n')

def load_tasks(filename="tasks.txt"):
    # Пытаемся открыть файл и загрузить задачи.
    try:
        with open(filename, 'r') as file:
            # Читаем строки из файла и убираем лишние пробелы/переносы.
            return [line.strip() for line in file]
    except FileNotFoundError:
        # Если файл не найден, возвращаем пустой список.
        return []

def show_tasks(tasks):
    # Проверяем, есть ли задачи в списке.
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Ваши задачи:")
        # Перебираем задачи и выводим их с номерами.
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Загружаем задачи из файла при старте программы.
tasks = load_tasks()

while True:
    # Ждем команду от пользователя.
    command = input("Введите команду (add, show, delete, exit): ").strip().lower()

    if command == 'add':
        # Добавляем новую задачу.
        task = input("Введите задачу: ")
        tasks.append(task)
        print(f"Задача '{task}' добавлена!")

    elif command == 'show':
        # Показываем все задачи.
        show_tasks(tasks)

    elif command == 'delete':
        # Показываем список задач перед удалением.
        show_tasks(tasks)
        try:
            # Запрашиваем у пользователя номер задачи для удаления.
            index = int(input("Введите номер задачи для удаления: ")) - 1
            # Проверяем, что номер задачи корректный.
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)  # Удаляем задачу из списка.
                print(f"Задача '{removed_task}' удалена!")
            else:
                print("Неверный номер задачи.")
        except ValueError:
            # Если пользователь ввел не число, выводим сообщение об ошибке.
            print("Пожалуйста, введите число.")

    elif command == 'exit':
        # Сохраняем все задачи и выходим из программы.
        save_tasks(tasks)
        print("Задачи сохранены. До встречи!")
        break

    else:
        # Если команда неизвестна, просим повторить ввод.
        print("Неизвестная команда. Попробуйте снова.")
