
from rich.console import Console
from rich.table import Table

# Инициализация консоли
console = Console()

# Данные для Kanban-доски
kanban_data = {
    "Backlog (Задачи в очереди)": [
        "Добавить систему уровней для героев",
        "Внедрить различные типы героев (воин, маг, лучник)",
        "Добавить систему инвентаря и предметов",
        "Разработать возможность прокачки характеристик",
        "Внедрить систему специальных умений",
        "Добавить сохранение и загрузку игры",
        "Разработать режим сражения с несколькими противниками",
        "Создать систему достижений"
    ],
    "To Do (Запланировано)": [
        "Улучшить визуальное представление HP-баров",
        "Добавить анимацию для ударов",
        "Расширить вариативность атак",
        "Реализовать возможность выбора действий в бою (атака, защита, использование предмета)"
    ],
    "In Progress (В работе)": [
        "Создать базовую структуру классов",
        "Реализовать базовый игровой процесс",
        "Добавить случайные вариации урона"
    ],
    "Testing (Тестирование)": [
        "Протестировать базовую механику боя",
        "Проверить корректность отображения статуса героев"
    ],
    "Done (Выполнено)": [
        "Спроектировать класс Hero",
        "Спроектировать класс Game",
        "Реализовать метод attack",
        "Реализовать метод is_alive",
        "Реализовать отображение статуса героев",
        "Реализовать систему раундов",
        "Добавить критические удары",
        "Реализовать случайный выбор первого хода",
        "Добавить возможность играть повторно"
    ]
}

# Создание таблицы Kanban
kanban_table = Table(title="Kanban доска: Битва героев", show_header=True, header_style="bold magenta")

# Добавление колонок
for column in kanban_data.keys():
    kanban_table.add_column(column, style="cyan", width=30)

# Добавление задач (максимальное количество строк)
max_rows = max(len(tasks) for tasks in kanban_data.values())
for i in range(max_rows):
    row = []
    for column in kanban_data.keys():
        tasks = kanban_data[column]
        if i < len(tasks):
            row.append(tasks[i])
        else:
            row.append("")
    kanban_table.add_row(*row)

# Вывод таблицы
console.print(kanban_table)