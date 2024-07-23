from faker import Faker
import queue
import uuid


# Створюэмо фейкер
fake = Faker()
# Створити чергу заявок
request_queue = queue.Queue()


# Генерація Id
def generate_unique_id():
    return str(uuid.uuid4())


def generate_request():
    request_id = generate_unique_id()

    # Створити нову заявку
    new_request = {"id": request_id, "text": fake.text()}

    # Додати заявку до черги
    request_queue.put(new_request)


def process_request():
    if not request_queue.empty():
        # Видалити заявку з черги
        current_request = request_queue.get()

        # Обробити заявку (можна вивести інформацію про обробку)
        print(
            f"Processing request with ID {current_request['id']}, text{current_request['text']}"
        )
    else:
        print("Request queue is empty")

# Головний цикл програми
while True:
    user_input = input("Press 'Enter' to continue or 'q' to quit: ")

    if user_input.lower() == "q":
        break

    # Створюємо нові заявки
    generate_request()

    # Оброблюємо заявки
    process_request()
