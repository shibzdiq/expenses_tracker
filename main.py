from db_manager import DatabaseManager

# Ініціалізація бази даних
db = DatabaseManager()
db.add_test_data()  # Додає тестові дані під час першого запуску

def display_menu():
    """Відображає меню для користувача"""
    print("\n1. Переглянути всі витрати")
    print("2. Додати нову витрату")
    print("3. Підрахувати загальну суму витрат")
    print("4. Вийти")

while True:
    display_menu()
    choice = input("Виберіть опцію: ")

    if choice == "1":
        expenses = db.view_expenses()
        print("=== Всі витрати ===")
        for expense in expenses:
            print(f"ID: {expense[0]}, Дата: {expense[1]}, Категорія: {expense[2]}, Сума: {expense[3]}, Опис: {expense[4]}")
    elif choice == "2":
        date = input("Введіть дату (YYYY-MM-DD): ")
        category = input("Введіть категорію: ")
        amount = float(input("Введіть суму: "))
        description = input("Введіть опис: ")
        db.add_expense(date, category, amount, description)
        print("Витрати успішно додано!")
    elif choice == "3":
        total = db.total_expenses()
        print(f"Загальна сума витрат: {total:.2f} грн" if total else "Немає записів про витрати.")
    elif choice == "4":
        db.close_connection()
        print("До побачення!")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
